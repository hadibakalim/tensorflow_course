#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'tensorflow_course\Lesson 1'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# ##### Copyright 2018 The TensorFlow Authors.

#%%
#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#%% [markdown]
# ## **Introduction to Colab and Python**
#%% [markdown]
# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l01c01_introduction_to_colab_and_python.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://github.com/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l01c01_introduction_to_colab_and_python.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />View source on GitHub</a>
#   </td>
# </table>
#%% [markdown]
# Welcome to this Colab where you will get a quick introduction to the Python programming language and the environment used for the course's exercises: Colab.
# 
# Colab is a Python development environment that runs in the browser using Google Cloud. 
# 
# For example, to print "Hello World", just hover the mouse over [  ] and press the play button to the upper left. Or press shift-enter to execute.

#%%
# Never mind this statement, for compatibility reasons
from __future__ import absolute_import, division, print_function, unicode_literals


#%%
print("Hello World")

#%% [markdown]
# ## Functions, Conditionals, and Iteration
# Let's create a Python function, and call it from a loop.

#%%
def HelloWorldXY(x, y):
  if (x < 10):
    print("Hello World, x was < 10")
  elif (x < 20):
    print("Hello World, x was >= 10 but < 20")
  else:
    print("Hello World, x was >= 20")
  return x + y

for i in range(8, 25, 5):  # i=8, 13, 18, 23 (start, stop, step)
  print("--- Now running with i: {}".format(i))
  r = HelloWorldXY(i,i)
  print("Result from HelloWorld: {}".format(r))


#%%
print(HelloWorldXY(1,2))

#%% [markdown]
# Easy, right?
# 
# If you want a loop starting at 0 to 2 (exclusive) you could do any of the following

#%%
print("Iterate over the items. `range(2)` is like a list [0,1].")
for i in range(2):
  print(i)

print("Iterate over an actual list.")
for i in [0,1]:
  print(i)

print("While works")
i = 0
while i < 2:
  print(i)
  i += 1


#%%
print("Python supports standard key words like continue and break")
while True:
  print("Entered while")
  break

#%% [markdown]
# ## Numpy and lists
# Python has lists built into the language.
# However, we will use a library called numpy for this.
# Numpy gives you lot's of support functions that are useful when doing Machine Learning.
# 
# Here, you will also see an import statement. This statement makes the entire numpy package available and we can access those symbols using the abbreviated 'np' syntax.

#%%
import numpy as np  # Make numpy available using np.

# Create a numpy array, and append an element
a = np.array(["Hello", "World"])
a = np.append(a, "!")
print("Current array: {}".format(a))
print("Printing each element")
for i in a:
  print(i)

print("\nPrinting each element and their index")
for i,e in enumerate(a):
  print("Index: {}, was: {}".format(i, e))


#%%
print("\nShowing some basic math on arrays")
b = np.array([0,1,4,3,2])
print("Max: {}".format(np.max(b)))
print("Average: {}".format(np.average(b)))
print("Max index: {}".format(np.argmax(b)))


#%%
print("\nYou can print the type of anything")
print("Type of b: {}, type of b[0]: {}".format(type(b), type(b[0])))


#%%
print("\nUse numpy to create a [3,3] dimension array with random number")
c = np.random.rand(3, 3)
print(c)


#%%
print("\nYou can print the dimensions of arrays")
print("Shape of a: {}".format(a.shape))
print("Shape of b: {}".format(b.shape))
print("Shape of c: {}".format(c.shape))
print("...Observe, Python uses both [0,1,2] and (0,1,2) to specify lists")

#%% [markdown]
# ## Colab Specifics
#%% [markdown]
# Colab is a virtual machine you can access directly. 
# To run commands at the VM's terminal, prefix the line with an exclamation point (!).
# 
# 

#%%
print("\nDoing $ls on filesystem")
get_ipython().system('ls -l')
get_ipython().system('pwd')


#%%
print("Install numpy")  # Just for test, numpy is actually preinstalled in all Colab instancs
get_ipython().system('pip install numpy')

#%% [markdown]
# **Exercise**
# 
# Create a code cell underneath this text cell and add code to:
# 
# 
# *   List the path of the current directory (pwd)
# * Go to / (cd) and list the content (ls -l)

#%%
get_ipython().system('pwd')
get_ipython().system('cd /')
get_ipython().system('ls -l')
print("Hello")

#%% [markdown]
# All usage of Colab in this course is completely free or charge. Even GPU usage is provided free of charge for some hours of usage every day.
# 
# **Using GPUs**
# * Many of the exercises in the course executes more quickly by using GPU runtime: Runtime | Change runtime type | Hardware accelerator | GPU
# 
# **Some final words on Colab**
# *   You execute each cell in order, you can edit & re-execute cells if you want
# *   Sometimes, this could have unintended consequences. For example, if you add a dimension to an array and execute the cell multiple times, then the cells after may not work. If you encounter problem reset your environment:
#   *   Runtime -> Restart runtime... Resets your Python shell
#   *   Runtime -> Restart all runtimes... Will reset the Colab image, and get you back to a 100% clean environment
# * You can also clear the output in the Colab by doing: Edit -> Clear all outputs
# * Colabs in this course are loaded from GitHub. Save to your Google Drive if you want a copy with your code/output: File -> Save a copy in Drive...
# 
# **Learn More**
# *   Check out [this](https://www.youtube.com/watch?v=inN8seMm7UI&list=PLQY2H8rRoyvwLbzbnKJ59NkZvQAW9wLbx&index=3) episode of #CodingTensorFlow, and don't forget to subscribe to the YouTube channel ;)
# 

