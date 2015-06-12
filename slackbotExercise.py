import random
import time
import requests
import json
import csv

USERTOKENSTRING =  # YOUR (SLACKBOT API) USER AUTH TOKEN
URLTOKENSTRING =  # SLACKBOT REMOTE CONTROL URL TOKEN
#Esta funcion no es necesario retocarla
def extractSlackUsers(token):
    # Set token parameter of Slack API call
    tokenString = token
    params = {"token": tokenString}

    # Capture Response as JSON
    response = requests.get("https://slack.com/api/users.list", params=params)
    users = json.loads(response.text, encoding='utf-8')["members"]

    def findUserNames(x):
        if getStats(x) == False:
            return None
        name = "@" + x["name"].encode('utf-8')
        return name.encode('utf-8')
    def getStats(x):
        params = {"token": tokenString, "user": x["id"]}
        response = requests.get("https://slack.com/api/users.getPresence",
                params=params)
        status = json.loads(response.text, encoding='utf-8')["presence"]
        return status == "active"

    return filter(None, list(map(findUserNames, users)))
#Cambiamos los valores de esta funcion al castellano
def selectExerciseAndStartTime():

    # Ejercicios (2 tipos de  Strings)
    exercises = [" FLEXIONES ", " FLEXIONES ", " CRUNCH ", " SENTADILLAS ", " ZANCADAS "]
    exerciseAnnouncements = ["FLEXIONES", "FLEXIONES", "PLANCHA", "SENTADILLAS", "PIERNAS"]

    # Generador de random para los intervalos de tiempo y los ejercicios
    nextTimeInterval = random.randrange(300, 1800)
    exerciseIndex = random.randrange(0, 5)

    # Anuncio de sorteo
    lotteryTimeString = "EL SIGUIENTE SORTEO DE  " + str(exerciseAnnouncements[exerciseIndex]) + " ES DENTRO DE " + str(nextTimeInterval/60) + " MINUTOS."

    requests.post("https://ctrlla.slack.com/services/hooks/slackbot?token="+URLTOKENSTRING+"&channel=%23general", data=lotteryTimeString)

    time.sleep(nextTimeInterval)

    return str(exercises[exerciseIndex])

#Traducimos este tambien
def selectPerson(exercise):

    # Seleccionamos numero de repeticiones, downgrade a intervalo de 10-30
    exerciseReps = random.randrange(10, 30)

    # Sacar usuarios de la API
    slackUsers = extractSlackUsers(USERTOKENSTRING)

    # Seleccionar indice de usuario
    selection = random.randrange(0, len(slackUsers))

    lotteryWinnerString = str(exerciseReps) + str(exercise) + "AHORA MISMO " + slackUsers[selection]
    print lotteryWinnerString
    requests.post("https://ctrlla.slack.com/services/hooks/slackbot?token="+URLTOKENSTRING+"&channel=%23general", data=lotteryWinnerString)

    with open("results.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([slackUsers[selection], exerciseReps, exercise])

for i in range(10000):
    exercise = selectExerciseAndStartTime()
    selectPerson(exercise)


