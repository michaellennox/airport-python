#Airport Challenge - Python

This is a repeat of the [airport-challenge](https://github.com/makersacademy/airport_challenge) written in Python instead of the original Ruby. You can find my original Ruby solution [at this repo](https://github.com/michaellennox/airport_challenge).

I have aimed to solve this challenge in a test driven manner with automated feature and unit tests using the unittest library.

##Installation Instructions

Clone the repository then change directory into it.

```
$ git clone git@github.com:michaellennox/oystercard-python.git
$ cd oystercard-python
```

Install and activate VirtualEnv

```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Install required packages using pip and the requirements.txt file

```
$ pip install -r requirements.txt
```

Open the interpreter and import the application files

```python
$ python
>>>
```

Now you can use the airport system.

##Usage Instructions

##Brief

We have a request from a client to write the software to control the flow of planes at an airport. The planes can land and take off provided that the weather is sunny. Occasionally it may be stormy, in which case no planes can land or take off. Here are the user stories that we worked out in collaboration with the client:

###User Stories

```
As an air traffic controller
So I can get passengers to a destination
I want to instruct a plane to land at an airport and confirm that it has landed

As an air traffic controller
So I can get passengers on the way to their destination
I want to instruct a plane to take off from an airport and confirm that it is no longer in the airport

As an air traffic controller
To ensure safety
I want to prevent takeoff when weather is stormy

As an air traffic controller
To ensure safety
I want to prevent landing when weather is stormy

As an air traffic controller
To ensure safety
I want to prevent landing when the airport is full

As the system designer
So that the software can be used for many different airports
I would like a default airport capacity that can be overridden as appropriate
```

##Contributors

* [Michael Lennox](https://github.com/michaellennox) - michael@michaellennox.me
