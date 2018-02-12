{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 3, 4]"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from collections import Counter\n",
    "def mean(*args):\n",
    "    return sum(*args)/len(*args)\n",
    "    \n",
    "\n",
    "def median(s):\n",
    "    s = sorted(s)\n",
    "    return s[(int(len(s)/2))]\n",
    "\n",
    "def mode(s):\n",
    "    c = Counter(s)\n",
    "    c =dict(c)\n",
    "    return [k for k, v in c.items() if v == max(c.values())]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.0\n",
      "[1, 2, 3]\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "from collections import Counter\n",
    "class stats():\n",
    "\n",
    "    def mean(*args):\n",
    "        return sum(*args)/len(*args)\n",
    "    \n",
    "\n",
    "    def median(s):\n",
    "        s = sorted(s)\n",
    "        return s[(int(len(s)/2))]\n",
    "\n",
    "    def mode(s):\n",
    "        c = Counter(s)\n",
    "        c =dict(c)\n",
    "        return [k for k, v in c.items() if v == max(c.values())]\n",
    "r = [1,2,3]\n",
    "print(stats.mean(r))\n",
    "print(stats.mode(r))\n",
    "print(stats.median(r))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
