{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOBv9EEKAkHY8DJYUX9qhCP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Amirisettyrohith/python-basics-assignment/blob/main/python_basics_%3CAmirisetty_Rohith%3E.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nQJpXsjqFstz",
        "outputId": "439053fa-604d-45c8-e873-135b05df3b26"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter name:Rohith\n",
            "Enter age:20\n",
            "Enter height:6.1\n",
            "True/False:True\n",
            "Rohith 20 6.1 True\n",
            "Name:Rohith | Age:20 | Height:6.1 | Student:True\n",
            "Age in months: 240\n",
            "Age in days: 7300\n",
            "Remainder when age is divided by 7: 6\n",
            "Age raised to power of 2: 400\n"
          ]
        }
      ],
      "source": [
        "name=input(\"Enter name:\")\n",
        "age=int(input(\"Enter age:\"))\n",
        "height=float(input(\"Enter height:\"))\n",
        "student=bool(input(\"True/False:\"))\n",
        "print(name,age,height,student)\n",
        "print(f\"Name:{name} | Age:{age} | Height:{height} | Student:{student}\")\n",
        "print(\"Age in months:\",age*12)\n",
        "print(\"Age in days:\",age*365)\n",
        "print(\"Remainder when age is divided by 7:\",age%7)\n",
        "print(\"Age raised to power of 2:\",age**2)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "NMiNZgA0GaYg"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}