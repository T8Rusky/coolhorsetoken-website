from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template for the Website
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CoolHorseToken (CHT)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f4f4f9;
            color: #333;
        }
        header {
            background: #222;
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }
        .container {
            max-width: 1000px;
            margin: 20px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #444;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        ul li {
            padding: 5px 0;
        }
        footer {
            text-align: center;
            padding: 10px;
            background: #222;
            color: #fff;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>CoolHorseToken (CHT)</h1>
        <p>The Future of Meme Coins</p>
    </header>
    <div class="container">
        <h2>Our Vision</h2>
        <p>CoolHorseToken represents speed, innovation, and the future of meme coins. It's designed to appeal to a fun-loving, tech-savvy community with a shared love for crypto and creativity.</p>

        <h2>Tokenomics</h2>
        <ul>
            <li><strong>Total Supply:</strong> 1 billion CHT</li>
            <li><strong>Distribution:</strong></li>
            <ul>
                <li>50% Community Rewards & Airdrops</li>
                <li>20% Liquidity Pool</li>
                <li>15% Development Fund</li>
                <li>10% Marketing & Partnerships</li>
                <li>5% Team Allocation</li>
            </ul>
        </ul>

        <h2>Use Cases</h2>
        <ul>
            <li>Gamification: Mini-games where players can use CHT to upgrade their cool horse avatars.</li>
            <li>NFT Marketplace: Purchase and trade horse-themed NFTs with exclusive traits and benefits.</li>
            <li>Staking: Earn rewards for holding CHT and contributing to network liquidity.</li>
            <li>Merchandise: Exclusive access to branded CoolHorse merchandise.</li>
        </ul>

        <h2>Ecosystem Features</h2>
        <ul>
            <li><strong>NeonStable:</strong> A DeFi hub for staking and yield farming.</li>
            <li><strong>CyberRanch:</strong> A marketplace for unique horse-themed NFTs.</li>
            <li><strong>GallopSwap:</strong> A decentralized exchange tailored for meme coins.</li>
        </ul>

        <h2>Marketing Strategy</h2>
        <ul>
            <li>Viral social media campaigns featuring the cool horse mascot.</li>
            <li>Collaborations with influencers in the crypto and meme spaces.</li>
            <li>NFT giveaways and airdrops to build an engaged community.</li>
            <li>Merchandise drops tied to token milestones.</li>
        </ul>

        <h2>Roadmap</h2>
        <h3>Phase One: Foundation</h3>
        <ul>
            <li>Develop token and smart contract.</li>
            <li>Launch website and social channels.</li>
            <li>Initial NFT collection release.</li>
        </ul>
        <h3>Phase Two: Growth</h3>
        <ul>
            <li>Build NeonStable and CyberRanch platforms.</li>
            <li>Execute airdrops and launch on DEXs.</li>
            <li>Partner with meme coin communities.</li>
        </ul>
        <h3>Phase Three: Expansion</h3>
        <ul>
            <li>Launch GallopSwap.</li>
            <li>List on CEXs and expand NFT offerings.</li>
            <li>Integrate gamification and metaverse features.</li>
        </ul>
    </div>
    <footer>
        <p>&copy; 2024 CoolHorseToken. All Rights Reserved.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
