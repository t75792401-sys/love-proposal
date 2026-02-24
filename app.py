from flask import Flask, render_template_string

app = Flask(__name__, static_folder="static")

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For My Love ❤️</title>

<style>
body{
    margin:0;
    padding:0;
    overflow:hidden;
    background:black;
    font-family: 'Segoe UI', sans-serif;
    color:white;
    text-align:center;
}

/* Animated Galaxy */
body::before{
    content:"";
    position:fixed;
    width:200%;
    height:200%;
    background: radial-gradient(circle at 30% 30%, #ff0080, transparent 40%),
                radial-gradient(circle at 70% 70%, #7928ca, transparent 40%),
                radial-gradient(circle at 50% 50%, #2afadf, transparent 40%);
    animation: moveBg 25s linear infinite;
    z-index:-1;
}
@keyframes moveBg{
    from{ transform:translate(0,0);}
    to{ transform:translate(-25%,-25%);}
}

.container{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
}

button{
    padding:15px 35px;
    margin:15px;
    font-size:1.2rem;
    border-radius:30px;
    border:none;
    cursor:pointer;
    transition:0.3s;
}

.yes{ background:#ff0055; color:white;}
.no{ background:#555; color:white;}
button:hover{ transform:scale(1.15); }

.hidden{ display:none; }

/* Glow Name */
.glow{
    font-size:6vw;
    font-weight:bold;
    color:#ff4dff;
    text-shadow:
        0 0 10px #ff4dff,
        0 0 20px #ff00cc,
        0 0 40px #ff00cc,
        0 0 80px #ff00cc;
    animation:pulse 2s infinite alternate;
}
@keyframes pulse{
    from{ text-shadow:0 0 20px #ff4dff;}
    to{ text-shadow:0 0 60px #ff00cc;}
}

/* Fade in photo */
.photo{
    width:250px;
    border-radius:20px;
    margin:20px;
    opacity:0;
    animation:fadeIn 3s forwards;
}
@keyframes fadeIn{
    to{ opacity:1;}
}

/* Typing effect */
.typing{
    font-size:1.5rem;
    width:80%;
    margin:auto;
    border-right:3px solid white;
    white-space:nowrap;
    overflow:hidden;
}

/* Hearts */
.heart{
    position:absolute;
    color:#ff3366;
    font-size:20px;
    animation:float 6s linear infinite;
}
@keyframes float{
    from{ transform:translateY(100vh); opacity:1;}
    to{ transform:translateY(-10vh); opacity:0;}
}
</style>
</head>

<body>

<div class="container" id="question">
    <h1>Do you know what’s the day today? 💖</h1>
    <button class="yes" onclick="startLove()">YES</button>
    <button class="no" onclick="startLove()">NO</button>
</div>

<div class="container hidden" id="love">
    <div class="glow">SUMAYYA ANJUM</div>
    <img src="/static/her.jpg" class="photo">
    <div id="typedText" class="typing"></div>
</div>

<audio id="music" loop>
  <source src="/static/perfect.mp3" type="audio/mpeg">
</audio>

<script>
const text = "One year ago we started something beautiful... ❤️ Today we complete one year together. You are my happiness, my peace, my forever. I love you meri jaan so much. Will you stay with me forever? 💍";

function startLove(){
    document.getElementById("question").classList.add("hidden");
    document.getElementById("love").classList.remove("hidden");
    document.getElementById("music").play();
    typeWriter();
    createHearts();
}

function typeWriter(){
    let i=0;
    function typing(){
        if(i<text.length){
            document.getElementById("typedText").innerHTML += text.charAt(i);
            i++;
            setTimeout(typing,50);
        }
    }
    typing();
}

function createHearts(){
    setInterval(()=>{
        const heart=document.createElement("div");
        heart.className="heart";
        heart.innerHTML="❤";
        heart.style.left=Math.random()*100+"vw";
        heart.style.fontSize=Math.random()*20+10+"px";
        document.body.appendChild(heart);
        setTimeout(()=>heart.remove(),6000);
    },300);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)