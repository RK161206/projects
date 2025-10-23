CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    review_text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO reviews (customer_name, review_text, rating) 
VALUES 
('Sarah', 'Loved the service! Will come back again.', 5),
('James', 'Good experience overall, but delivery was a bit late.', 4),
('Amira', 'The coffee is amazing, perfect atmosphere.', 5);
SELECT review_id, customer_name, review_text, rating, created_at
FROM reviews
ORDER BY created_at DESC;
