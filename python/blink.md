## **Blinker**
---
- Subscribing to Signals & Emitting Signals
~~~python
[in]
from blinker import signal

def subscriber(sender):
    print("Got a signal sent by %r" % sender)

class Processor:
  def __init__(self, name):
    self.name = name

  def go(self):
    ready = signal('ready')
    ready.send(self)
    print("Processing.")
    complete = signal('complete')
    complete.send(self)

  def __repr__(self):
    return '<Processor %s>' % self.name


ready = signal('ready')
ready.connect(subscriber)
processor_a = Processor('a')
processor_a.go()

[out]
Got a signal sent by <Processor a>
Processing.
~~~

- Subscribing to Specific Senders
~~~python
[in]
def b_subscriber(sender):
  print("Caught signal from processor_b.")
  assert sender.name == 'b'
processor_b = Processor('b')
ready.connect(b_subscriber, sender=processor_b)
processor_a.go()
processor_b.go()

[out]
Got a signal sent by <Processor b>
Caught signal from processor_b.
Processing.
~~~
- Sending and Receiving Data Through Signals
~~~python
[in]
send_data = signal('send-data')
@send_data.connect
def receive_data(sender, **kw):
  print("Caught signal from %r, data %r" % (sender, kw))
  return 'received!'

result = send_data.send('anonymous', abc=123)
print(result)
# The return value of send() collects the return values of each connected function as a list of (receiver function, return value) pairs:

[out]
Caught signal from 'anonymous', data {'abc': 123}
[(<function receive_data at 0x...>, 'received!')]
~~~

- Practicle Example
~~~python
[in]
from blinker import signal
frobnicated = signal('frobnicated')

class Receiver(object):

  def __init__(self):
    def handle_frobnicated(sender, **kwargs):
      self.on_frobnicated(sender, **kwargs)
    self.handle_frobnicated = handle_frobnicated
    frobnicated.connect(handle_frobnicated)

  def on_frobnicated(self, sender, **kwargs):
    print sender, kwargs['message']

if __name__ == '__main__':
  receiver = Receiver()
  for i in range(10):
      frobnicated.send('Sender %s' % i, message='hello')

[out]
Sender 0 hello
Sender 1 hello
Sender 2 hello
Sender 3 hello
Sender 4 hello
Sender 5 hello
Sender 6 hello
Sender 7 hello
Sender 8 hello
Sender 9 hello
~~~
