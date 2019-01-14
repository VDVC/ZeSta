# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("ZeSta.tsv", sep="\t")

df.drop('Stelle', axis=1, inplace=True)
df.drop('Beschluss', axis=1, inplace=True)
df.drop('Titel', axis=1, inplace=True)

df = df[df.Release != 2019]

counts = pd.crosstab(df.Release, df.Einstufung, margins=False)

freigaben = ['18',   'Cut',    'o.R.',    'A',       'B',    'Beschl.']
farben =    ['blue', 'red', 'lightgrey', 'darkred', 'grey', 'black']

counts = counts[freigaben]

counts.plot(kind='bar', stacked=True, color=farben)

plt.grid(axis='y')
plt.ylabel("Anzahl")

plt.savefig("Zesta_2018.png")

