#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, knowledge):
        self.knowledge = []
    
    def learn(self, string):
        self.knowledge.append(string)