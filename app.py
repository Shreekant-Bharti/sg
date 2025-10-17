from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Personalize this with your girlfriend's name
GIRLFRIEND_NAME = "Shristi"

# Store messages in a JSON file
MESSAGES_FILE = 'messages.json'

# Initialize messages file if it doesn't exist
if not os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump({
            "love_notes": [
                "Shristi, you are the most beautiful chapter of my life story. 💝",
                "Every sunrise with you feels like the first day of forever. 🌅",
                "Your presence makes every ordinary moment extraordinary. 🌹",
                "With you, even the simplest moments become the best memories. ✨",
                "You're not just my love, you're my home, my peace, my everything. 💕"
            ],
            "surprises": [
                "Remember our first time in the temple? That's when I knew you were a blessing. 🙏✨",
                "Our color coordination wasn't just about clothes, it was our souls matching. 💕💖",
                "That first sunrise with you? Best feeling ever, watching a new beginning together. 🌄",
                "The hall, the temple, every place becomes special when you're there with me. 💫",
                "You make every 'meet' more than just a bahana - it's where my heart belongs. 🥰"
            ],
            "future_promises": [
                "I promise to watch a thousand more sunrises with you, each one more beautiful. 🌅💍",
                "We'll create countless more 'best memories' that will last forever. 📸",
                "I'll always be there to color coordinate with you - in life, in love, in everything. 👫",
                "Every temple visit, every hall moment, every random pic will be a treasure. 🙏",
                "I promise to make every feeling with you the 'best feeling ever'. ❤️"
            ],
            "compliments": [
                "Shristi, your smile is the most beautiful thing I've ever witnessed. 😊✨",
                "You have a soul so pure, it makes everything around you glow. 💎",
                "The way you look at life with such grace and beauty inspires me daily. 🌺",
                "You're not just gorgeous on the outside, your heart is even more beautiful. 💖",
                "Every moment I spend with you reminds me why I'm the luckiest person alive. 🌟"
            ],
            "custom_messages": []
        }, f, indent=4)

def load_messages():
    """Load messages from JSON file"""
    with open(MESSAGES_FILE, 'r') as f:
        return json.load(f)

def save_messages(messages):
    """Save messages to JSON file"""
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=4)

@app.route('/')
def index():
    """Render the main romantic page"""
    messages = load_messages()
    
    # 120 Reasons Why I Love You, Shristi
    reasons_i_love_you = [
        "I love the way you look at me.",
        "You make me feel like I'm the only person in the world.",
        "With you I can be myself.",
        "I love you because we are family and friends at the same time.",
        "When we're together, all my problems disappear.",
        "You make my heart smile.",
        "You know me better than I know myself.",
        "You are always willing to help me accomplish my goals.",
        "You have the smoothest skin. I could spend hours just watching and caressing it.",
        "You make me smile when nobody else can.",
        "You have taught me the true meaning of love.",
        "Because I miss you… even when you're in the next room.",
        "Because when I'm hurt, you help clean me up and bandage me and kiss and make it better.",
        "You're always there for me, no matter what.",
        "I love when we walk down the street in the rain, and you hold the umbrella above me so I don't get wet.",
        "You let me be myself and you encourage me to find more of myself.",
        "You are truthful and vulnerable with me.",
        "You encourage me after I feel like I've failed.",
        "You make me feel like I can get through anything, as long as I have you.",
        "You sacrifice and work so hard, without even realizing that you are.",
        "You love my family, even though they're crazy!",
        "You take care of me and spoil me when I'm sick.",
        "You always make time for just the two of us.",
        "Because you are determined to make this relationship work.",
        "Because you help me see negative things differently.",
        "Because when you laugh it makes me laugh!",
        "We understand each other so well.",
        "Your arms feel more like home than any house ever did.",
        "You have an inner strength that helps keep me calm when my life is in chaos.",
        "You always keep your promises.",
        "You help me understand technology, without being condescending.",
        "You have the ability to comfort me simply by your touch.",
        "You always apologize first, no matter who's wrong.",
        "Because you are so sexy and I can't believe I get to call you mine.",
        "Because you always swap the wet towels for dry ones when you know I'm showering after you.",
        "Because when things don't go as planned, you roll with it, instead of getting stressed.",
        "You always believe in me and inspire me.",
        "I can always talk to you.",
        "You give me massages.",
        "Because I can see how much you love being there for me.",
        "I love you because you picked me.",
        "Your eyes smile when you laugh.",
        "You kiss me goodbye when I'm still asleep in the morning.",
        "You let me pick the movie.",
        "You are sweeter than my favorite dessert.",
        "You love me even when I'm being horrible and hard to be around.",
        "Because you always treat everyone well.",
        "We're so different and yet so the same.",
        "You are doing everything to become a better person for yourself and for us.",
        "You make an effort with my friends and family, because you know how much they mean to me.",
        "I love how you put so much thought into everything you do for me.",
        "You have an innate ability to protect and take care of me.",
        "I love you because you gave me the gift of yourself.",
        "You make me a better person.",
        "I love you every time you reach across our bed to pull me close to you.",
        "Because you make me feel special.",
        "You have a gentle and calming voice that soothes me when I'm upset.",
        "The day I met you, I found my missing piece.",
        "Because I can be myself around you.",
        "Because you trust me unconditionally.",
        "You are always pushing me to be better and my biggest fan in all that I do.",
        "You make all of my dreams come true, no matter how small they are.",
        "You make me laugh so hard that I spit my drink out!",
        "Your willingness always to try new things make my life full of adventures.",
        "You are always kind to other people, even if they don't deserve it.",
        "Because I can't imagine life without you.",
        "You know the secret, little things that cheer me up and make me happy.",
        "You only seem to notice my strengths and always have confidence in me.",
        "You don't just tell me you love me, you show me.",
        "You know how to cheer me up when I'm sad.",
        "You care deeply about my success and my happiness.",
        "You never give up on me, even when I'm at my worst.",
        "You turn on the seat warmer in the car for me.",
        "You follow me and you push me.",
        "You're smart and dedicated to your job.",
        "You always have an idea of something fun to do.",
        "You make me feel completely cherished and adored.",
        "You care about the people around you.",
        "You are patient and loving with those close to you.",
        "You always tip.",
        "You're always there when I need a shoulder to cry on.",
        "You are smoking hot!",
        "I love your snuggles.",
        "You may not always agree with my decisions but you always trust me to make them.",
        "I love that you ask about my day.",
        "You have the courage to chase your dreams.",
        "You still give me butterflies.",
        "You tell great stories.",
        "You are great at giving people compliments.",
        "You're cute when you're grumpy.",
        "I love that your hand fits perfectly with mine.",
        "I love that I get to go through life with you.",
        "When we go places together, you pitch in to make the trips easier and more fun.",
        "We spend lots of time talking about decisions we need to make together.",
        "You tell me why you love me.",
        "You'll do my chores when you know I've had a bad day.",
        "When I do your chores or pick up the slack around the house, you always noticed.",
        "You are my very best friend in the whole world.",
        "You always open the car door for me.",
        "You make the dark a little less scary.",
        "You're the calm in the storm.",
        "You make me feel so safe.",
        "I love how you're able to make me laugh, even when the situation shouldn't be funny.",
        "You are everything I never knew I needed.",
        "I love that you let me cuddle up REALLY close to you… even when you're overheating.",
        "You hold my hand in movies.",
        "When you're a guest in someone's home you always eat what they've prepared, even if you're not a huge fan.",
        "You give up your seat for the elderly.",
        "You're not afraid to be silly with me.",
        "You're always saving funny memes on your phone to show me later because you want me to laugh too.",
        "I love that you make my fears melt away.",
        "When you talk to people you're focused on them.",
        "You put other's needs before your own.",
        "Your kisses make me weak in the knees.",
        "I love that you take care of me when I forget to.",
        "You're always doing little, creative things to let me know you care.",
        "You wake up with a smile in the morning.",
        "You know when to help and when to let me do it myself.",
        "You always carry heavy bags for me.",
        "You're a great person to talk decisions over with. You don't tell me what I should do but you give me great feedback and listen."
    ]
    
    # Our special memories with personalized captions
    our_memories = [
        {
            'image': 'first_time_in_temple.jpg',
            'caption': 'Our First Time in Temple Together 🙏',
            'quote': 'That moment I knew you were a blessing sent from above'
        },
        {
            'image': 'first_time_colour_cordination.jpg',
            'caption': 'First Time We Color Coordinated 💕',
            'quote': 'When our outfits matched, but our hearts were already in sync'
        },
        {
            'image': 'first_sunrise_with_uhh.jpg',
            'caption': 'Our First Sunrise Together 🌅',
            'quote': 'Watching the world wake up while falling deeper in love with you'
        },
        {
            'image': 'first_time_in_hall.jpg',
            'caption': 'Our First Time in the Hall ✨',
            'quote': 'Every place becomes magical when I am with you'
        },
        {
            'image': 'best_memory.jpg',
            'caption': 'Our Best Memory Together 💖',
            'quote': 'This moment will forever be etched in my heart'
        },
        {
            'image': 'best_feeling_ever.jpg',
            'caption': 'The Best Feeling Ever 🥰',
            'quote': 'Being with you feels like home, like peace, like everything right'
        },
        {
            'image': 'meet_ek_bahana.jpg',
            'caption': 'Meet? Ek Bahana Hai 😊',
            'quote': 'Every excuse to see you becomes the highlight of my day'
        },
        {
            'image': 'rendom_pic.jpg',
            'caption': 'Just a Random Beautiful Moment 📸',
            'quote': 'Even random moments with you are picture perfect'
        },
        {
            'image': 'IMG-20251015-WA0011.jpg',
            'caption': 'A Special Captured Moment 💝',
            'quote': 'Some moments are too precious to not be captured forever'
        }
    ]
    
    return render_template('index.html', 
                         girlfriend_name=GIRLFRIEND_NAME,
                         love_notes=messages['love_notes'],
                         custom_messages=messages['custom_messages'],
                         memories=our_memories,
                         reasons=reasons_i_love_you)

@app.route('/get-surprise')
def get_surprise():
    """Get a random surprise message"""
    import random
    messages = load_messages()
    
    surprise_type = request.args.get('type', 'surprises')
    
    if surprise_type in messages and messages[surprise_type]:
        surprise = random.choice(messages[surprise_type])
        return jsonify({'success': True, 'message': surprise, 'type': surprise_type})
    
    return jsonify({'success': False, 'message': 'No surprises available'})

@app.route('/add-message', methods=['POST'])
def add_message():
    """Add a new custom message"""
    data = request.get_json()
    message = data.get('message', '').strip()
    
    if message:
        messages = load_messages()
        messages['custom_messages'].append({
            'text': message,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        save_messages(messages)
        return jsonify({'success': True, 'message': 'Message added successfully!'})
    
    return jsonify({'success': False, 'message': 'Message cannot be empty'})

@app.route('/get-all-messages')
def get_all_messages():
    """Get all custom messages"""
    messages = load_messages()
    return jsonify({'success': True, 'messages': messages['custom_messages']})

@app.route('/get-random-reason')
def get_random_reason():
    """Get a random reason why I love you"""
    import random
    
    reasons = [
        "I love the way you look at me.",
        "You make me feel like I'm the only person in the world.",
        "With you I can be myself.",
        "I love you because we are family and friends at the same time.",
        "When we're together, all my problems disappear.",
        "You make my heart smile.",
        "You know me better than I know myself.",
        "You are always willing to help me accomplish my goals.",
        "You have the smoothest skin. I could spend hours just watching and caressing it.",
        "You make me smile when nobody else can.",
        "You have taught me the true meaning of love.",
        "Because I miss you… even when you're in the next room.",
        "Because when I'm hurt, you help clean me up and bandage me and kiss and make it better.",
        "You're always there for me, no matter what.",
        "I love when we walk down the street in the rain, and you hold the umbrella above me so I don't get wet.",
        "You let me be myself and you encourage me to find more of myself.",
        "You are truthful and vulnerable with me.",
        "You encourage me after I feel like I've failed.",
        "You make me feel like I can get through anything, as long as I have you.",
        "You sacrifice and work so hard, without even realizing that you are.",
        "You love my family, even though they're crazy!",
        "You take care of me and spoil me when I'm sick.",
        "You always make time for just the two of us.",
        "Because you are determined to make this relationship work.",
        "Because you help me see negative things differently.",
        "Because when you laugh it makes me laugh!",
        "We understand each other so well.",
        "Your arms feel more like home than any house ever did.",
        "You have an inner strength that helps keep me calm when my life is in chaos.",
        "You always keep your promises.",
        "You help me understand technology, without being condescending.",
        "You have the ability to comfort me simply by your touch.",
        "You always apologize first, no matter who's wrong.",
        "Because you are so sexy and I can't believe I get to call you mine.",
        "Because you always swap the wet towels for dry ones when you know I'm showering after you.",
        "Because when things don't go as planned, you roll with it, instead of getting stressed.",
        "You always believe in me and inspire me.",
        "I can always talk to you.",
        "You give me massages.",
        "Because I can see how much you love being there for me.",
        "I love you because you picked me.",
        "Your eyes smile when you laugh.",
        "You kiss me goodbye when I'm still asleep in the morning.",
        "You let me pick the movie.",
        "You are sweeter than my favorite dessert.",
        "You love me even when I'm being horrible and hard to be around.",
        "Because you always treat everyone well.",
        "We're so different and yet so the same.",
        "You are doing everything to become a better person for yourself and for us.",
        "You make an effort with my friends and family, because you know how much they mean to me.",
        "I love how you put so much thought into everything you do for me.",
        "You have an innate ability to protect and take care of me.",
        "I love you because you gave me the gift of yourself.",
        "You make me a better person.",
        "I love you every time you reach across our bed to pull me close to you.",
        "Because you make me feel special.",
        "You have a gentle and calming voice that soothes me when I'm upset.",
        "The day I met you, I found my missing piece.",
        "Because I can be myself around you.",
        "Because you trust me unconditionally.",
        "You are always pushing me to be better and my biggest fan in all that I do.",
        "You make all of my dreams come true, no matter how small they are.",
        "You make me laugh so hard that I spit my drink out!",
        "Your willingness always to try new things make my life full of adventures.",
        "You are always kind to other people, even if they don't deserve it.",
        "Because I can't imagine life without you.",
        "You know the secret, little things that cheer me up and make me happy.",
        "You only seem to notice my strengths and always have confidence in me.",
        "You don't just tell me you love me, you show me.",
        "You know how to cheer me up when I'm sad.",
        "You care deeply about my success and my happiness.",
        "You never give up on me, even when I'm at my worst.",
        "You turn on the seat warmer in the car for me.",
        "You follow me and you push me.",
        "You're smart and dedicated to your job.",
        "You always have an idea of something fun to do.",
        "You make me feel completely cherished and adored.",
        "You care about the people around you.",
        "You are patient and loving with those close to you.",
        "You always tip.",
        "You're always there when I need a shoulder to cry on.",
        "You are smoking hot!",
        "I love your snuggles.",
        "You may not always agree with my decisions but you always trust me to make them.",
        "I love that you ask about my day.",
        "You have the courage to chase your dreams.",
        "You still give me butterflies.",
        "You tell great stories.",
        "You are great at giving people compliments.",
        "You're cute when you're grumpy.",
        "I love that your hand fits perfectly with mine.",
        "I love that I get to go through life with you.",
        "When we go places together, you pitch in to make the trips easier and more fun.",
        "We spend lots of time talking about decisions we need to make together.",
        "You tell me why you love me.",
        "You'll do my chores when you know I've had a bad day.",
        "When I do your chores or pick up the slack around the house, you always noticed.",
        "You are my very best friend in the whole world.",
        "You always open the car door for me.",
        "You make the dark a little less scary.",
        "You're the calm in the storm.",
        "You make me feel so safe.",
        "I love how you're able to make me laugh, even when the situation shouldn't be funny.",
        "You are everything I never knew I needed.",
        "I love that you let me cuddle up REALLY close to you… even when you're overheating.",
        "You hold my hand in movies.",
        "When you're a guest in someone's home you always eat what they've prepared, even if you're not a huge fan.",
        "You give up your seat for the elderly.",
        "You're not afraid to be silly with me.",
        "You're always saving funny memes on your phone to show me later because you want me to laugh too.",
        "I love that you make my fears melt away.",
        "When you talk to people you're focused on them.",
        "You put other's needs before your own.",
        "Your kisses make me weak in the knees.",
        "I love that you take care of me when I forget to.",
        "You're always doing little, creative things to let me know you care.",
        "You wake up with a smile in the morning.",
        "You know when to help and when to let me do it myself.",
        "You always carry heavy bags for me.",
        "You're a great person to talk decisions over with. You don't tell me what I should do but you give me great feedback and listen."
    ]
    
    reason_number = random.randint(1, 120)
    reason = random.choice(reasons)
    
    return jsonify({
        'success': True, 
        'reason': reason,
        'number': reason_number
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
