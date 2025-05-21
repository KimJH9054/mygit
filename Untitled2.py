#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine started with {self.horsepower} horsepower.")

