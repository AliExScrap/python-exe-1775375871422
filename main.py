import webview
import os

# Le code HTML/CSS/JS de la calculatrice
html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Calculatrice</title>
    <style>
        body { background: #1a1a1a; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; overflow: hidden; }
        .calc { width: 320px; background: #2d2d2d; padding: 15px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        #screen { width: 100%; height: 60px; font-size: 32px; text-align: right; background: transparent; border: none; color: #00ff88; margin-bottom: 15px; outline: none; }
        .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
        button { height: 60px; border-radius: 8px; border: none; background: #3d3d3d; color: white; font-size: 20px; cursor: pointer; transition: 0.2s; }
        button:hover { background: #4d4d4d; }
        button:active { transform: scale(0.95); }
        .op { background: #ff9500; color: white; }
        .op:hover { background: #ffaa33; }
        .eq { background: #00ff88; color: #1a1a1a; grid-column: span 2; font-weight: bold; }
        .eq:hover { background: #33ffaa; }
        .clr { color: #ff4444; }
    </style>
</head>
<body>
    <div class="calc">
        <input type="text" id="screen" readonly value="0">
        <div class="grid">
            <button class="clr" onclick="clr()">C</button>
            <button onclick="add('/')">/</button>
            <button onclick="add('*')">×</button>
            <button onclick="del()">⌫</button>
            
            <button onclick="add('7')">7</button>
            <button onclick="add('8')">8</button>
            <button onclick="add('9')">9</button>
            <button class="op" onclick="add('-')">-</button>
            
            <button onclick="add('4')">4</button>
            <button onclick="add('5')">5</button>
            <button onclick="add('6')">6</button>
            <button class="op" onclick="add('+')">+</button>
            
            <button onclick="add('1')">1</button>
            <button onclick="add('2')">2</button>
            <button onclick="add('3')">3</button>
            <button class="eq" onclick="calc()">=</button>
            
            <button onclick="add('0')" style="grid-column: span 2;">0</button>
            <button onclick="add('.')">.</button>
        </div>
    </div>
    <script>
        const s = document.getElementById('screen');
        function add(v) { if(s.value==='0' && v!=='.') s.value=v; else s.value+=v; }
        function clr() { s.value='0'; }
        function del() { s.value = s.value.length > 1 ? s.value.slice(0,-1) : '0'; }
        function calc() { try { s.value = eval(s.value.replace('×', '*')); } catch { s.value = 'Erreur'; } }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    # Créer une fenêtre native qui charge le contenu HTML
    webview.create_window('Ma Calculatrice HTML', html=html_content, width=360, height=520, resizable=False)
    webview.start()
