from django.shortcuts import render

# Create your views here.

import string
from django.shortcuts import render
import docx2txt as dt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def main(request):
    return render(request,"index.html")
def check_strength(request):
    val=request.POST['description']
    val1=request.POST['resume']
# resume=dt.process(val1)
    content=[val,val1]
    cv=CountVectorizer()
    matrix=cv.fit_transform(content)
    similarity_matrix=cosine_similarity(matrix)
    value="{:.2f}".format(similarity_matrix[0][1]*100)
    value=float(value)
    if(value>=65.0):
        result="Hurray!! Your resume fits for this Role.. Keep going"
    elif(value<65.0 and value>30.0):
        result="Oops, Your resume needs to update with some skills, kindly modify and recheck the strength"
    else:
        result="Nope, Your resume won't make for this Role, kindly rebuild your resume. "
    return render(request,'index.html',{"res":result,"val":value,"col":"green"})

if __name__=='__main__':
    main()