{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f33f0359",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$cbfBPHH-)52\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "def generate_password(length=12):\n",
    "    characters = string.ascii_letters + string.digits + string.punctuation\n",
    "    return ''.join(random.choice(characters) for _ in range(length))\n",
    "\n",
    "password = generate_password()\n",
    "print(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0a7031a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "06c66bc6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "JFzc%dlWecqd\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import string\n",
    "\n",
    "def generate_password(length=12):\n",
    "    characters = string.ascii_letters + string.digits + string.punctuation\n",
    "    return ''.join(random.choice(characters) for _ in range(length))\n",
    "\n",
    "password = generate_password()\n",
    "print(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adfa4758",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
