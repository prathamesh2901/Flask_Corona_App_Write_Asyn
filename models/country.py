import pika



class CountryModel():


    def __init__(self, name, cases, deaths, recoveries):
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries

    def json(self):
        return {'name': self.name, 'cases': self.cases, 'deaths': self.deaths, 'recoveries': self.recoveries}

    def send_to_queue(self):
        credentials = pika.PlainCredentials('pratham2901', 'Corona99')
        connection = pika.BlockingConnection(pika.ConnectionParameters('10.0.0.42',credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue='hello',durable=True)
        body = f"{{name: {self.name}, cases: {self.cases}, deaths: {self.deaths}, recoveries: {self.recoveries}}}"
        channel.basic_publish(exchange='', routing_key='hello', body=body)
        connection.close()
