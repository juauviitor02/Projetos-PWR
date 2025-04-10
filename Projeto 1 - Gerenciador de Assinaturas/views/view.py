import __init__
from models.database import engine
from models.model import Subscription, Payment
from sqlmodel import Session, SQLModel, select
from datetime import date, datetime

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            return subscription

    def list_all_subscriptions(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement)
            return results.all()

    def list_all_payments(self):
        with Session(self.engine) as session:
            statement = select(Payment)
            results = session.exec(statement)
            return results.all()
    
    def delete_subscription(self, id):
        with Session(self.engine) as session:
            while True:
                statement = select(Subscription).where(Subscription.id == id)
                result = session.exec(statement).one()
                question = input(f"Você deseja remover a assinatura {result.empresa}? Y ou N: ")
                if question.upper() == "Y":
                    session.delete(result)
                    session.commit()
                    print("Assinatura removida com sucesso!")
                return

    def delete_payment(self, id):
        with Session(self.engine) as session:
            while True:
                statement = select(Payment).where(Payment.id == id)
                result = session.exec(statement).one()
                question = input(f"Você deseja remover o pagamento da assinatura {result.empresa}? Y ou N: ")
                if question.upper() == "Y":
                    session.delete(result)
                    session.commit()
                    print("Pagamento removido com sucesso!")
                return

    def _has_pay_(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False

    def pay(self, subscription: Subscription):
        with Session(self.engine) as session:
            statement = select(Payment).join(Subscription).where(Subscription.id == subscription.id)
            results = session.exec(statement).all()
          
            if self._has_pay_(results):
                question = input("Essa conta já foi paga esse mês. Deseja pagar novamente? Y ou N: ")
                if not question.upper() == "Y":
                    return
               
            pay = Payment(subscription_id=subscription.id, empresa=subscription.empresa, date=date.today())
            session.add(pay)
            session.commit()
            print("Pagamento efetuado com sucesso!")          

    def total_value(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            results = session.exec(statement)
            total = 0
            for result in results:
               total += result.valor
            
            return float(total)

    def _get_last_12_months_native(self):
        today = datetime.now()
        year = today.year
        month = today.month
        last_12_months = []
        for i in range(12):
            last_12_months.append((month, year))
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        
        return last_12_months[::-1]
    
    def _get_value_for_months(self, last_12_months):
        with Session(self.engine) as session:
            statement = select(Payment)
            results = session.exec(statement).all()
            
            value_for_months = []
            for i in last_12_months:
                value = 0
                for result in results:
                    if result.date.month == i[0] and result.date.year == i[1]:
                        value += float(result.subscription_id)
                value_for_months.append(value)
            return value_for_months
            
    
    def get_chart(self):
        last_12_months = self._get_last_12_months_native()
        value_for_months = self._get_value_for_months(last_12_months)
        
        last_12_months2 = list(map(lambda x: x[0], self._get_last_12_months_native()))
        '''last_12_months2 = []
        for i in last_12_months:
            last_12_months2.append(i[0])
        print(value_for_months)
        print(last_12_months2)'''

        last_12_months3 = []
        for i in range(1, 13):
            last_12_months3.append(i)
        print(value_for_months)
        print(last_12_months2)

        import matplotlib.pyplot as plt
        plt.plot(last_12_months3, value_for_months)
        plt.show()

ss = SubscriptionService(engine)
'''subscription = Subscription(empresa="Empresa 1", site="www.empresa1.com", data_assinatura=date.today(), valor=110.0)
ss.create(subscription)
subscription = Subscription(empresa="Empresa 2", site="www.empresa2.com", data_assinatura=date.today(), valor=120.0)
ss.create(subscription)
subscription = Subscription(empresa="Empresa 3", site="www.empresa3.com", data_assinatura=date.today(), valor=130.0)
ss.create(subscription)
subscription = Subscription(empresa="Empresa 4", site="www.empresa4.com", data_assinatura=date.today(), valor=140.0)
ss.create(subscription)
subscription = Subscription(empresa="Empresa 5", site="www.empresa5.com", data_assinatura=date.today(), valor=150.0)
ss.create(subscription)'''
'''assinaturas = ss.list_all_subscriptions()
for i, s in enumerate(assinaturas):
    print(f"[{i}] - {s.empresa}")
ss.pay(assinaturas[int(input("Digite o número que corresponde a empresa que deseja pagar: "))])'''
#print(ss.total_value())
'''assinaturas = ss.list_all_subscriptions()
print("Assinaturas cadastradas:")
for n, i in enumerate(assinaturas):
    print(f"[{n}] - {i.id} - {i.empresa}")
print(ss.delete_subscription(int(input("Informe o id da assinatura: "))))'''
'''assinaturas = ss.list_all_payments()
print("Pagamentos cadastrados:")
for n, i in enumerate(assinaturas):
    print(f"[{n}] - {i.subscription_id} - {i.empresa}")
print(ss.delete_payment(int(input("Informe o id da assinatura: "))))'''
#print(ss._get_last_12_months_native())
#print(ss._get_value_for_months(ss._get_last_12_months_native()))
#print(ss.get_chart())

