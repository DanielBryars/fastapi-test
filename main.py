from fastapi import FastAPI
from typing import Optional
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/prediction",summary="Get a predicted score", description="""
         
<h2 style="margin-bottom: 0">They’ve done studies, you know. 65% of the time...</h2>
<h3 style="margin-top: 0">...it works every time.</h3>
                  
<div style="display: flex; gap: 20px; align-items: flex-start;">
    <img src="/static/brian-fantana.jpg" alt="Brian Fantana" width="300"/>
    <img src="/static/data-score-histogram.png" alt="Score Histogram" width="625"/>
</div>              
         """)
def get_prediction(title: str, url: Optional[str] = None):
    return {"predicted_score": 2}
