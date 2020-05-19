import pika

class StateModel():


    def __init__(self, name, today, cases, deaths, recoveries):
        self.name = name
        self.today = today
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries

    def json(self):
        return {"name": self.name, "date": self.today, "cases": self.cases, "deaths": self.deaths, "recoveries": self.recoveries}

    def send_to_queue(self):
        credentials = pika.PlainCredentials('pratham2901', 'Corona99')
        connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.42',credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='hello',durable=True)
        body = "{{ \"name\": \"{0}\", \"date\": \"{1}\", \"cases\": \"{2}\", \"deaths\": \"{3}\", \"recoveries\": \"{4}\" }}".format(self.name,self.today,self.cases,self.deaths,self.recoveries)
        channel.basic_publish(exchange='', routing_key='hello', body=body)
        connection.close()
