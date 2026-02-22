from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
PASSWORD = "29072005"

login_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Solo para Vivi 🌙</title>
<style>
body{
margin:0;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:black;
font-family:Arial;
color:white;
text-align:center;
}
.box{
background:rgba(255,255,255,0.05);
padding:30px;
border-radius:20px;
backdrop-filter:blur(15px);
width:90%;
max-width:350px;
}
input{
padding:10px;
border-radius:10px;
border:none;
width:80%;
}
button{
margin-top:15px;
padding:10px 20px;
border:none;
border-radius:10px;
background:#ff4b7d;
color:white;
}
</style>
</head>
<body>
<div class="box">
<h2>🌌 Solo para Vivi ✨</h2>
<p>Ingresa tu fecha especial (DDMMAAAA)</p>
<form method="POST">
<input type="password" name="password" placeholder="29072005">
<br>
<button type="submit">Entrar</button>
</form>
</div>
</body>
</html>
"""

romantic_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Para Vivi 💖</title>
<style>
body{
margin:0;
overflow:hidden;
background:black;
color:white;
font-family:Arial;
text-align:center;
}

.nebula{
position:fixed;
width:100%;
height:100%;
background:
radial-gradient(circle at 30% 40%, rgba(255,0,150,0.2), transparent 40%),
radial-gradient(circle at 70% 60%, rgba(0,150,255,0.2), transparent 40%);
animation:rotate 60s linear infinite;
}
@keyframes rotate{
from{transform:rotate(0deg);}
to{transform:rotate(360deg);}
}

.star{
position:absolute;
width:2px;
height:2px;
background:white;
border-radius:50%;
animation:twinkle 3s infinite alternate;
}
@keyframes twinkle{
from{opacity:0.2;}
to{opacity:1;}
}

h1{
margin-top:40px;
font-size:clamp(40px,8vw,70px);
animation:glow 3s infinite alternate;
}
@keyframes glow{
from{text-shadow:0 0 15px #ff6bcb;}
to{text-shadow:0 0 35px #ffffff;}
}

.card{
width:90%;
max-width:700px;
margin:20px auto;
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:20px;
backdrop-filter:blur(8px);
font-size:clamp(16px,3vw,20px);
line-height:1.7;
}

.planet{
position:fixed;
bottom:-120px;
left:50%;
transform:translateX(-50%);
width:300px;
height:300px;
border-radius:50%;
background:radial-gradient(circle at 30% 30%, #3a86ff, #000814);
box-shadow:0 0 80px rgba(58,134,255,0.5);
animation:spin 80s linear infinite;
}
@keyframes spin{
from{transform:translateX(-50%) rotate(0deg);}
to{transform:translateX(-50%) rotate(360deg);}
}

.asteroid{
position:absolute;
font-size:30px;
animation:asteroid 10s linear infinite;
}
@keyframes asteroid{
0%{transform:translate(-10vw,20vh);}
100%{transform:translate(110vw,70vh);}
}

.spaceship{
position:absolute;
font-size:30px;
animation:ship 18s linear infinite;
}
@keyframes ship{
0%{transform:translate(110vw,10vh);}
100%{transform:translate(-10vw,60vh);}
}

#mensajeFinal{
margin-top:20px;
color:#ff9ff3;
font-weight:bold;
}

#post{
display:none;
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
background:black;
color:white;
justify-content:center;
align-items:center;
flex-direction:column;
text-align:center;
font-size:28px;
}

.final-btn{
margin-top:20px;
padding:15px 30px;
border:none;
border-radius:30px;
background:linear-gradient(45deg,#ff4b7d,#ff6bcb);
color:white;
font-size:18px;
cursor:pointer;
box-shadow:0 0 15px #ff6bcb;
transition:0.3s;
}

.final-btn:hover{
transform:scale(1.1);
box-shadow:0 0 30px #ff6bcb;
}

#finalRing{
margin-top:25px;
font-size:90px;
animation:float 3s ease-in-out infinite alternate;
}

@keyframes float{
from{transform:translateY(0px);}
to{transform:translateY(-20px);}
}
</style>
</head>
<body>

<div class="nebula"></div>
<div class="planet"></div>

<audio id="music" loop>
<source src="/static/music.mp3" type="audio/mpeg">
</audio>

<h1>Vivi ✨</h1>
<h3 id="contador"></h3>

<div class="card">
Vivi…  
Puede que a veces me cueste demostrarlo,  
pero lo que siento por ti es real.  
Estoy aprendiendo a quererte mejor cada día.
</div>

<div id="mensajeFinal"></div>

<div class="asteroid">☄️</div>
<div class="spaceship">🚀</div>

<div id="post">
✨ Continuará... ✨<br>
¿Quieres seguir escribiendo esta historia conmigo? 💖
<button class="final-btn" onclick="mostrarAnillo()">Sí, quiero 💞</button>
<div id="finalRing"></div>
</div>

<script>
// estrellas
for(let i=0;i<400;i++){
let s=document.createElement("div");
s.className="star";
s.style.top=Math.random()*100+"vh";
s.style.left=Math.random()*100+"vw";
s.style.animationDuration=(2+Math.random()*3)+"s";
document.body.appendChild(s);
}

// contador
function contador(){
const inicio=new Date("2025-08-21T00:00:00");
const ahora=new Date();
const diff=ahora-inicio;
const dias=Math.floor(diff/(1000*60*60*24));
const horas=Math.floor((diff/(1000*60*60))%24);
const minutos=Math.floor((diff/(1000*60))%60);
const segundos=Math.floor((diff/1000)%60);
document.getElementById("contador").innerHTML=
"💞 "+dias+" días "+horas+"h "+minutos+"m "+segundos+"s juntos 💞";
}
setInterval(contador,1000);
contador();

// música fade in
document.body.addEventListener("click",function(){
let m=document.getElementById("music");
m.volume=0;
m.play();
let fade=setInterval(()=>{
if(m.volume<0.8){m.volume+=0.02;}
else{clearInterval(fade);}
},200);
},{once:true});

// mensaje letra por letra
let texto="Si estás aquí... es porque quiero hacer las cosas bien contigo. 💖";
let i=0;
function escribir(){
if(i<texto.length){
document.getElementById("mensajeFinal").innerHTML+=texto.charAt(i);
i++;
setTimeout(escribir,60);
}
}
setTimeout(escribir,4000);

// post créditos
setTimeout(()=>{
document.getElementById("post").style.display="flex";
},25000);

// mostrar anillo
function mostrarAnillo(){
document.getElementById("finalRing").innerHTML="💍";
}
</script>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        if request.form["password"]==PASSWORD:
            return redirect(url_for("love"))
    return render_template_string(login_html)

@app.route("/love")
def love():
    return render_template_string(romantic_html)

if __name__=="__main__":
    app.run(debug=True)