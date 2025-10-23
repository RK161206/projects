from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Review Model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database
with app.app_context():
    db.create_all()

# Home route (optional)
@app.route('/')
def home():
    return "<h1>Welcome to Bean and Brew</h1><p><a href='/reviews'>Go to Reviews</a></p>"

# Reviews page
@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['review']
        rating = int(request.form['rating'])

        new_review = Review(customer_name=name, review_text=text, rating=rating)
        db.session.add(new_review)
        db.session.commit()

        return redirect('/reviews')

    all_reviews = Review.query.order_by(Review.created_at.desc()).all()
    return render_template('reviews.html', reviews=all_reviews)

if __name__ == "__main__":
    app.run(debug=True)
