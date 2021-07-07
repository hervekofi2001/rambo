from tchat.models import Article
def run():
    for i in range(7,14):
        article=Article()
        article.title="Article Num #%d " % i
        article.descrp="Description article Num #%id " % i
        article.image="http:/default"
        article.save()


print("succes de l'operation")
