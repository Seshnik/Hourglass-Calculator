# Hourglass PvP Calculator

**Hourglass PvP Calculator** is a tool for **Sea of Thieves**, specifically designed for the **Hourglass PvP** mode.
This application helps players calculate essential information related to leveling, including the optimal win streak to aim for based on their win rate, the estimated time required to reach a target level, and more.

## Features

- **Win Rate-Based Streak Suggestions**: Calculate the best win streak for your current win rate to maximize XP gains and reduce time spent leveling.
- **Leveling Calculator**: Input your current level and target level to see how many battles you need, total XP required, and the estimated time to reach the target.
- **Boost Support**: Includes calculations for various boost values like `Gold & Glory` and `Community Day` to account for XP bonuses.
- **Win Rate Calculator**: Integrated win-rate calculator and instructions on how to get this info from your account (Website or In-Game).

## How to Use

1. **Download the Program**: Download the `.exe` file from the [Releases](https://github.com/Seshnik/Hourglass-Calculator/releases) section and run it.
2. **Input Your Data**:
   - Enter your **current level** and **target level**.
   - Input your **win rate** and select the appropriate **boost** (if any).
     - You can Select the HELP menu and then select "Win-Rate" to open the Win Rate calculator.
     - You will need to provide the requested data needed. (Battles Completed, Battles Won, etc - It's all explained in the app)
3. **Get Results**:
   - The program will display:
     - The total XP required to reach your target level.
     - The best streak to aim for based on your win rate.
     - Estimated time to reach the target level, accounting for any streak resets and boosts.

## Installation

You can use the executable, though I know many may not trust .exe files, so the source code is available for those who want to run it that way.
I used Pyinstaller to create this .exe file, so you will need to do the same, though it can run out of the box through Python, without the need of converting it into an executable.

As always, Virus Scan every file you download, regardless of who or where you get it from.


## Credits

- [b_ootay_ful](https://www.reddit.com/user/b_ootay_ful/) - For their **PvP Tables: Exp gain, breakpoints** reddit post.
- [DavidSOT](https://www.youtube.com/@DavidSOT) - For their YouTube video **The Hourglass reputation system explained with data (Sea of Thieves)**
- [MassiveSponge](https://www.youtube.com/@massivesponge) - For their YouTube video **I SOLVED Sea of Thieves Hourglass | BEST STREAK FOUND** & their [Simulation code](https://github.com/massivesponge/hourglass-solve) that I used to help create my own code to determine Win-rate data.
