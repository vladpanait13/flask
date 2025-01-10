## DECORATORI

- functii care modifica comportamentul altei functii sau clase fara a schimba codul sursa
- folositi in logging, validare, autentificare sau modificarea functionalitatii existente
- o functie care modifica sau extinde comportamentul altei functii sau clase, pt a adauga o functionalitate fara a modifica functia/clasa originala

def decorator(functie):
def wrapper(*args, \*\*kwargs):
print("Inainte de a executa functia")
rezultat = functie(*args, \*\*kwargs)
print("Dupa ce functia a fost executata)
return rezultat
return wrapper

@decorator
def salut():
print("Salut!")
salut()

## GENERATORI

- tip special de functii care produc valori pe rand, folosind "yield"
- folositi pentru a economisi memorie si a genera secvente mari de date
- permit procesarea unui volum mare de date fara a le incarca toate in memorie
- ajuta la procesarea fisierelor mari, stream urilor de date sau secventelor infinite

- daca doresti sa returnezi o lista si nu ai nevoie de un generator, return este alegerea corecta. daca vrei sa creezi un generator care produce valori la cerere, 'yield' este solutia.

def_count_up_to(max):
count = 1
while count <= max:
yield count # cuvantul cheie "yield" care returneaza valoarea curenta a variabilei 'count'
count += 1

gen = count_up_to(5) # apelam functia cu argumentul 5 si stocam generatorul returnat in variabila 'gen'.acesta va produce numere de la 1 la 5 pe masura ce este iterat
for number in gen: # folosim un for pt a itera prin generatorul gen. valoarea returnata de yield va fi atribuita variabilei number, la fiecare iteratie
print(number)

## ITERATORI

- pot fi creati generatori manual folosind iter() si next(), permitand controlul manual al procesului de iteratie
- obiecte care implementeaza metodele ' ** iter ** ' si ' ** next ** '
- utilizati pentru a parcurge colectii de date fara a expune implementarea interna
- folositi in contextul stream-urilor de date sau algoritmilor care proceseaza date treptat

def simple_generator():
return iter([1,2,3,4,5])

gen = simple_generator()
for number in gen:
print(number)

## LIST COMPREHENSIONS

- expresii concise pentru a genera rapid liste
- pot fi folosite si pentru seturi si dictionare

lista = [x ** 2 for x in range(5) if x % 2 == 0]
print(lista)

## GLOBAL INTERPRETER LOCK

- mecanism care permite doar unui singur thread sa execute cod Python la un momentdat
- nu afecteaza sarcinile de tip I/O (unde asteptarea permite altor thread-uri sa ruleze)
- sarcinile intensive pe procesor nu pot beneficia de multithreading din cauza GIL
- simplicitate: simplifica gestionarea memoriei partajate
- performanta: pentru programe single-threaded, GIL poate imbunatati performanta

## MULTIPROCESSING

- creeaza procese separate, fiecare avand propriul interpretor Python si spatiu de memorie

- folosit pentru sarcini CPU-intensive (procesare de imagini, calcule matematice complexe)
- procesele ruleaza in paralel pe mai multe nuclee, facand o utilizare mai eficienta a nucleelor
- procesele ruleaza in spatii de memorie separate, comunicarea se face prin queues sau pipes

- ruleaza independent, fiecare cu memoria sa, permitand executia reala paralela, ocolind GIL

## MULTITHREADING

- permite rularea simultana a mai multor threads in acelasi proces.
- folosit pt sarcini I/O intensive (citirea fisierelor, cereri de retea, api calls)
- nu este recomandat pentru sarcini CPU-intensive din cauza GIL
- thread urile partajeaza acelasi spatiu de memorie, ceea ce necesita sincronizare
- sincronizarea se face folosing lock-uri

- permit executia simultana a mai multor sarcini usoare (in cadrul unui singur proces),
  dar sunt limitate de GIL (Global Interpreter Lock)

import threading |||||||||||||||||||||||||| from multiprocessing import Process

def functie(): |||||||||||||||||||||||||||| def functie():
print("Rulare intr-un thread nou") |||||||| print("Rulare intr-un proces nou)

thread = threading.Thread(target=functie) | proces = Process(target=functie)
thread.start() |||||||||||||||||||||||||||| proces.start()
thread.join() ||||||||||||||||||||||||||||| proces.join()

## CONTEXT MANAGERS

- gestioneaza automat resursele (ex fisiere, conexiuni) folosind "with"
- folosit la gestionarea resurselor care trebuie deschise si apoi eliberate, fisiere, conexiuni la baze de date

with open("fisier.txt", "r") as f:
continut = f.read()

## OOP DESIGN PATTERNS

- proiecte complexe care necesita reutilizare si extensibilitate
- design patterns: rezolvarea problemelor recurente (ex. Singleton, Factory, Observer)

## SQL

- bazat pe relatii(tabele)
- ideal pentru date structurate, interogari complexe
- folosit in aplicatii financiare, ERP, CRM

## NOSQL

- bazat pe documente, grafuri, key value pairs
- ideal pentru date nestructurate, aplicatii care cer scalabilitate mare
- folosit in aplicatii cu date dinamice, precum retelele sociale

## Optimizare SQL/INDEX coloane

- intr-o baza de date relationala, indecsii sunt structuri de date speciale care ajuta la imbunatatirea vitezei de cautare si a performantelor interogarilor SQL.
- functioneaza ca niste ghiduri rapide care ajuta sistemul de gestionare a bazelor de date (DBMS) sa gaseasca mai rapid datele fara a fi necesar sa parcurga intreaga tabela
- indecsii sunt folositi pentru optimizare, reducand timpul de cautare prin acces la date
- utili pe coloanele frecvent utilizate in filtrele de cautare sau in operatiuni de ordonare si combinare a tabelelor

CREATE INDEX idx_nume ON clienti(nume)

## Testare/Mocks

- un mock este un obiect fals care imita comportamentul unui obiect real, dar fara sa aiba functionalitate completa
- folosit pt a testa componente individuale fara sa depinzi de alte parti ale sistemului
  cand folosim mocks:
- izolare - pt a testa un modul fara sa depinzi de alte parti ale aplicatiei
- resurse externe - pentru a evita conexiuni reale la baze de date, api-uri sau alte sisteme externe
- control - pentru a simula scenarii greu de replicat (erori ale serverului, raspunsuri lente)

- evitarea costurilor - pt a nu trimite emailuri reale sau a nu accesa API-uri in timpul testarii

Cum se folosesc mocks?

- pt o functie simpla
  from unittest.mock import mock

def send_email(to, subject): # functia
print(f"Email trimis catre {to} cu subiectul {subiect}.") # Ar trimite un email real
send_email = Mock () # Mock-ul functiei
send_email("test@example.com", "Salut!") # Apelarea functiei
send_email.assert_called_with("test@example.com", "Salut!") # Verificare apeluri

- mock API uri externe
  import requests
  from unitest.mock import patch
  def get_weather(city): # Functie care face un request real
  response = request.get(f"http://api.weather.com/{city}")
  return response.json()

with patch('requests.get') as mocket_get:
mocked_get.return_value.json.return_value= {"temp": 20, "city": "Paris"}
weather = get_weather("Paris")
print(weather)

## Monolith

- o aplicatie unica, mare, care include toate functionalitatile
- exemplu o aplicatie de e-commerce unde frontend, backend si baza de date sunt intr-un singur proiect
- simplu de inceput, dezvoltarea si implementarea fiind mai rapide pt proiectele mici
- testare facila pt ca totul este intr-un singur loc
- usor de monitorizat, o singura aplicatie de urmarit
- dezavantaje: nu poti scala anumite parti ale aplicatiei, schimbarile majore pot afecta intregul sistem, devine greu de gestionat pe masura ce creste complexitatea

## Microservicii

- componente mici, independente, fiecare responsabila de o anumita functionalitate
- exemplu intr-o aplicatie de e-commerce, un microservice gestioneaza platile, altul produsele, altul users
- scalabilitate independenta, poti scala doar microserviciile care au nevoie
- flexibilitate tehnologica - fiecare microserviciu poate fi scris in limbajul potrivit
- fault tolerance - o eroare intr-un microservice nu afecteaza intreaga aplicatie
- fiecare echipa poate lucra la un microserviciu separat
- comunicare - necesita protocoale eficiente intre servicii (Rest)
- costuri operationale: mai multe instante, mai multe resurse
- debugging dificil
- securizare: utilizeaza OAuth sau JWT pentru a securiza accestul intre microservicii
- implementarea unui API Gateway pt a centraliza autentificarea

comunicare - microserv comunica in timp real, asteptand raspunsuri. protocol HTTP - ex un microservice pt users solicita detalii de la un microservice pt produse
comunicare - microserv comunica prin mesaje, fara a astepta raspunsuri. protocoale message brokers precum RabbitMQ, Kafka. exemplu - un microservice pentru comenzi trimite un mesaj catre microserviciul de livrare dupa procesarea unei comenzi

Alegi un monolit daca aplicatia e mica sau la inceput, vrei o solutie simpla, echipa de devs este mica
Alegi un microservice daca aplicatia e complexa si are multe functionalitati, ai nevoie de scalabilitate, echipele pot lucra independent.

## Docker

Docker este esential pt implementarea microserviciilor, oferind un mod simplu si eficient de a izola, implementa si scala serviciile.

## Celery

- permite aplicatiei tale sa indeplineasca sarcini in fundal, in loc sa le faca in timp ce utilizatorul asteapta
- exemplu cand trimiti un email dupa ce un user completeaza un formular, nu vrei ca aplicatia sa stea blocata pana cand emailul este trimis.
- cu celery poti programa sarcina de a trimite emailul sa fie executata in fundal

- producatorul de task-uri (producer) - aplicatia ta adauga task-uri intr-un queue
- broker de mesaje (message broker) - queue este gestionata de un broker de mesaje precum REDIS sau RabbitMQ, care stocheaza task-urile pana cand sunt preluate.
- worker-ul - este un proces separat care preia task-urile din queue si le executa
- poti folosi un backend (de ex Redis sau Postgresql) pt a stoca rezultatele task-urilor

- folosit pt api-uri externe care raspund lent, rapoarte zilnice, actualizari automate ale bazei de date

# Producatori-consumatori

- brutarie. brutaria face paine, clientii vin si o cumpara.
- producatorul este bucataria (ea produce painea - mesajele)
- consumatorul este clientul. el cumpara si mananca painea (proceseaza mesajele)
- painea este mesajele: producatorii trimit mesaje (creeaza painea), mesajele sunt puse intr-o coada (unde sta painea pe raft), consumatorii preiau mesajele din coada si le proceseaza (clientii iau painea de pe raft).
- producatorii si consumatorii sunt procese si aplicatii care comunica intre ele folosind mesaje

- producatorul poate fi o aplicatie care genereaza notificari. de exemplu "maria ti-a apreciat postarea"
- notificarea este pusa intr-o coada (ex gestionata de RabbitMQ sau Redis)
- consumatorul este un alt proces care preia mesajele si face ceva cu ele, cum ar fi sa trimita notificarea pe telefonul tau

## Redis

- aplicatiile pot stoca si gasi informatii, stocare pt acces rapid
- exemplu daca cauti "today weather" intr-o aplicatie, Redis poate pastra raspunsul pentru cateva ore, astfel incat aplicatia sa nu refaca aceeasi cerere mereu.
- message broker: poate fi folosit ca un sistem de queue pt a gestiona mesajele intre producatori si consumatori
- producatorii pun mesajele in coada, iar consumatorii le preiau
- stocare de date: poate pastra date simple, precum numere sau texte, dar si structuri complexe (liste, seturi, dictionare)
- stocheaza datele sub forma key-value pairs

- redis excelent pt aplicatii care necesita viteza mare si simplitate, RabbitMQ ideal pt gestionarea mesajelor complexe in sisteme distribuite, exemplu serverele amazon: unul gestioneaza comenzile, altul gestioneaza platile

## RabbitMQ

- gestioneaza queues, locuri unde mesajele sunt stocate temporar, asteptand sa fie preluate de consumatori
- producatorul creeaza si trimite mesaje catre RabbitMQ, exemplu o aplicatie care trimite notificari
- queues - mesajele sunt stocate aici pana cand un consumator vine sa le ia
- consumatorul preia mesajele din queue si le foloseste, exemplu o aplicatie trimite notificarea catre tlf tau

- producatorii si consumatorii nu comunica direct, RabbitMQ sau Redis sunt intermediarii.
- asigura ca mesajele nu se pierd
