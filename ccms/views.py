from django.shortcuts import render
from django.http import HttpResponse

def ccms_mission(request):
    mission = """<h1>CCMS Mission</h1>
    <p style="font-size:20px;">
        The College of Computing and Multimedia Studies shall produce competent and innovative professionals or 
        Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive 
        of national development goals and standards of global excellence.
    </p>"""
    return HttpResponse(mission)

def ccms_vision(request):
    vision = """<h1>CCMS Vision</h1>
    <p style="font-size:20px;">The College of Computing and Multimedia Studies shall be a center of excellence in delivering 
    Computing and Multimedia education.</p>"""
    return HttpResponse(vision)


def ccms_objectives(request):
    objectives = """<h1>CCMS Objectives</h1>
    <p style="font-size:20px;"> After graduation, alumni of MSEUF-CCS programs shall:</p>
    <ol style="font-size:20px;">
        <li>Be employed and demonstrate professionalism, competence and passion in solving contemporary problems by developing or utilizing innovative IT solutions;</li>
        <li>Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market; and</li>
        <li>Exhibit leadership and teamwork, and commitment to their respective local or global organizations.</li>
    </ol>"""
    return HttpResponse(objectives)