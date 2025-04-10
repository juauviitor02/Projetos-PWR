from ninja import Router, Schema, ModelSchema, Field, Body
from .schemas import LinkSchema, UpdateLinkSchema
from .models import *
from django.shortcuts import get_object_or_404, redirect
import qrcode
from io import BytesIO
import base64
from django.http import *



shortener_router = Router()

@shortener_router.post('create/', response={200: LinkSchema, 409: dict})
def create (request, link_schema: LinkSchema):
    data = link_schema.to_model_data()
    token = data['token']
    if token and Links.objects.filter(token=token).exists():
        return 409, {'error': 'Token já existe. Use outro token.'}
    redirect_link = data['redirect_link']
    expiration_time = data['expiration_time']
    max_unique_clicks = data['max_unique_clicks']
    link = Links(
        redirect_link=redirect_link,
        token=token,
        expiration_time=expiration_time,
        max_unique_clicks=max_unique_clicks,
    )
    link.save()
    return 200, link_schema.from_model(link)

@shortener_router.get('/{token}/', response={200: None, 404: dict})
def redirect_link(request, token):
    link = get_object_or_404(Links, token=token, active=True)

    if link.expired():
        return 404, {'error': 'Link expirado.'}
    
    unique_clicks = Clicks.objects.filter(link=link).values('ip_address').distinct().count()
    print(unique_clicks)
    if link.max_unique_clicks and unique_clicks >= link.max_unique_clicks:
        return 404, {'error': 'Limite de cliques atingido.'}
        
    click = Clicks(
        link=link,
        ip_address=request.META.get('REMOTE_ADDR')
    )    
    click.save()
    return redirect(link.redirect_link)

# Esse endpoint é para atualizar o link, token, tempo de expiração e cliques únicos
# Mas está dando erro 405 Method Not Allowed
# Não sei o porquê desse erro
# Vou deixar o código aqui para caso eu encontre a solução ou alguém saiba como resolver   
@shortener_router.put('/{link_id}/', response={200: UpdateLinkSchema, 404: dict})
def update_link(request, link_id: int, link_schema: UpdateLinkSchema =Body(...)):
    link = get_object_or_404(Links, id=link_id)
    data = link_schema.dict()
    token = data['token']
    if token and Links.objects.filter(token=token).exclude(id=link_id).exists():
        return 409, {'error': 'Token já existe. Use outro token.'}
    
    for field, value in data.items():
        if value is not None:
            setattr(link, field, value)
    link.save()
    return 200, link

@shortener_router.get('/statistics/{link_id}/', response={200: dict})
def statistics(request, link_id: int):
    links = get_object_or_404(Links, id=link_id)
    unique_clicks = Clicks.objects.filter(link=links).values('ip_address').distinct().count()
    total_clicks = Clicks.objects.filter(link=links).count()

    return {200: {'unique_clicks': unique_clicks, 'total_clicks': total_clicks}}

def get_api_url(request, token):
    scheme = request.scheme
    host = request.get_host()
    return f"{scheme}://{host}/api/{token}/"

@shortener_router.get('/qr-code/{link_id}/', response={200: dict})
def generate_qr_code(request, link_id: int):
    link = get_object_or_404(Links, id=link_id)
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(get_api_url(request, link.token))
    qr.make(fit=True)

    content = BytesIO()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(content)

    data = base64.b64encode(content.getvalue()).decode('utf-8')
    return 200, {'content_image': data}

