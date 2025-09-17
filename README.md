# <img src="asset/PlayerCar.png" alt="Player Car" width="30"/> Asphalt Escape <img src="asset/PoliceCar.png" alt="Police Car" width="30"/>

Um jogo desenvolvido em **Python + Pygame** como projeto de estudo da disciplina *Linguagem de Programação Aplicada* no curso de Análise e Desenvolvimento de Sistemas (UNINTER).  

## 🎮 Sobre o jogo
Você controla um carro que deve escapar do tráfego e evitar colisões.  
Enquanto o tempo passa, a velocidade da pista aumenta, deixando o desafio cada vez maior.  

### Mecânicas principais:
- 🏎️ Movimento lateral do carro do jogador (faixas da pista).  
- 🚓 Carro da polícia que persegue o jogador e pode provocar *Game Over* se houver colisão.  
- 🚧 Geração dinâmica de obstáculos.  
- ⏱️ Sistema de aceleração de velocidade conforme o tempo.  
- ⭐ Sistema de pontuação (10 pontos a cada segundo de sobrevivência).  

## 🛠️ Tecnologias
- [Python 3.12](https://www.python.org/)  
- [Pygame](https://www.pygame.org/news)  

## 📂 Estrutura do projeto
- `main.py` → ponto de entrada do jogo.  
- `Game.py` → gerencia o fluxo entre menu e fase.  
- `Level.py` → lógica principal do jogo.  
- `Entity/` → classes de entidades (PlayerCar, Obstacle, Background, etc.).  
- `Const.py` → constantes de configuração.  

## ▶️ Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/asphalt-escape.git
   cd asphalt-escape

    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt
    
   python main.py


## 📸 Screenshots

### Menu
![Menu](screenshots/Menu.png)

### Gameplay
![Gameplay](screenshots/Gameplay.png)

## 📚 Aprendizados

Estruturação de um projeto em múltiplos arquivos Python.

Uso de eventos do Pygame (timers, inputs, colisões).

Controle de velocidade e aceleração com base em clock.tick().

Manipulação de listas de entidades em tempo real.

## ✨ Próximos passos

Melhorar o design gráfico.

Adicionar efeitos sonoros para colisão.

Adicionar efeitos de luzes nos carrinhos.

Etc...