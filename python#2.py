{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5fac2284-9550-431b-8ce4-f1eafab7123f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original dictionary: {'name': 'John', 'age': 25, 'address': 'New York'}\n",
      "Updated dictionary: {'name': 'John', 'age': 25, 'address': 'New York', 'phone': '1234567890'}\n"
     ]
    }
   ],
   "source": [
    "person = {\n",
    "    'name': 'John',\n",
    "    'age': 25,\n",
    "    'address': 'New York'}\n",
    "print(\"Original dictionary:\", person)\n",
    "\n",
    "person['phone'] = '1234567890'\n",
    "print(\"Updated dictionary:\", person)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d8215747-c672-4b01-a953-85366b8ba8d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original set: {1, 2, 3, 4, 5}\n",
      "Set after adding 6: {1, 2, 3, 4, 5, 6}\n",
      "Set after removing 3: {1, 2, 4, 5, 6}\n"
     ]
    }
   ],
   "source": [
    "my_set = {1, 2, 3, 4, 5}\n",
    "print(\"Original set:\", my_set)\n",
    "my_set.add(6)\n",
    "print(\"Set after adding 6:\", my_set)\n",
    "my_set.discard(3)\n",
    "print(\"Set after removing 3:\", my_set)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1372d194-3cd0-4709-b02c-9052c9399e7b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tuple: (1, 2, 3, 4)\n",
      "Length of the tuple: 4\n"
     ]
    }
   ],
   "source": [
    "my_tuple = (1, 2, 3, 4)\n",
    "print(\"Tuple:\", my_tuple)\n",
    "\n",
    "print(\"Length of the tuple:\", len(my_tuple))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0dad616-b05f-4737-ba8d-bdf62dded034",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
