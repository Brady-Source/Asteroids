

https://github.com/user-attachments/assets/f409922e-2c5a-418b-be3b-f44fa96d1d08

# Asteroids

A classic Asteroids arcade game clone built with Python and Pygame. Pilot your ship, destroy incoming asteroids, and survive as long as possible — the asteroids keep coming!

## Demo

<video width="60%" controls muted playsinline>
  <source src="https://github.com/user-attachments/assets/f409922e-2c5a-418b-be3b-f44fa96d1d08" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Features

- Classic Asteroids gameplay with smooth 60 FPS rendering
- Asteroids split into smaller pieces when shot
- Score tracking displayed on screen (10 points per asteroid destroyed)
- Shooting cooldown system to balance gameplay
- Game Over screen with restart functionality
- Structured game state management (`RUNNING` / `GAME_OVER` phases)
- Built-in event and state logging via `logger.py`

## Tech Stack

| Tool    | Version |
|---------|---------|
| Python  | ≥ 3.13  |
| Pygame  | 2.6.1   |

## Getting Started

### Prerequisites

- Python 3.13+
- [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`

### Installation

**Using `uv` (recommended):**

```bash
git clone https://github.com/Brady-Source/Asteroids.git
cd Asteroids
uv sync
uv run main.py
```

**Using `pip`:**

```bash
git clone https://github.com/Brady-Source/Asteroids.git
cd Asteroids
pip install pygame==2.6.1
python main.py
```

## Controls

| Key     | Action         |
|---------|----------------|
| `W`     | Thrust forward |
| `A`     | Rotate left    |
| `D`     | Rotate right   |
| `Space` | Shoot          |

## Configuration

Game parameters can be adjusted in `constants.py`:

| Constant | Default | Description |
|----------|---------|-------------|
| `SCREEN_WIDTH` | 1280 | Window width (px) |
| `SCREEN_HEIGHT` | 720 | Window height (px) |
| `PLAYER_SPEED` | 200 | Player movement speed |
| `PLAYER_TURN_SPEED` | 200 | Rotation speed (deg/s) |
| `ASTEROID_SPAWN_RATE_SECONDS` | 0.8 | Time between asteroid spawns |
| `ASTEROID_KINDS` | 3 | Number of asteroid size tiers |
| `PLAYER_SHOOT_SPEED` | 500 | Projectile speed |
| `PLAYER_SHOOT_COOLDOWN_SECONDS` | 0.3 | Minimum time between shots |

## Project Structure
