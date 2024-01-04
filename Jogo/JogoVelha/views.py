from django.shortcuts import render
from .models import JogoVelha


# def index(request):
#     nome = "maicom"

#     return render(request, "JogoVelha/index.html", {"nome": nome})


def jogo(request):
    # Lógica para recuperar o estado do jogo e renderizar a página do jogo
    jogo = JogoVelha.objects.first()

    links = [
        {"url": "https://www.link1.com", "nome": "Link 1"},
        {"url": "https://www.link2.com", "nome": "Link 2"},
        {"url": "https://www.link3.com", "nome": "Link 3"},
    ]

    links2 = [
        {"url": "https://www.linkedin.com/mwlite/in/guilherme-benjamim-sordi-ba04551a1",
            "icone": "linkedin-ico.png"},
        {"url": "https://github.com/gu1lh3rm3s0rd1?tab=repositories",
            "icone": "github-ico.png"},
        {"url": "https://www.instagram.com/guilhermesordi_/", "icone": "insta-ico.png"},
    ]

    return render(request, "JogoVelha/jogo.html", {
        "jogo": jogo,
        'links': links,
        'links2': links2
    })


def index(request):
    links = [
        {"url": "https://www.link1.com", "nome": "Link 1"},
        {"url": "https://www.link2.com", "nome": "Link 2"},
        {"url": "https://www.link3.com", "nome": "Link 3"},
    ]

    links2 = [
        {"url": "https://www.linkedin.com/mwlite/in/guilherme-benjamim-sordi-ba04551a1",
            "icone": "linkedin-ico.png"},
        {"url": "https://github.com/gu1lh3rm3s0rd1?tab=repositories",
            "icone": "github-ico.png"},
        {"url": "https://www.instagram.com/guilhermesordi_/", "icone": "insta-ico.png"},
    ]

    return render(request, "JogoVelha/index.html", {
        'links': links,
        'links2': links2,
        # 'icones': icones
    })
