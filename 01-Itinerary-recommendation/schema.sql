-- Create cities table
CREATE TABLE cities (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT,
    description TEXT,
    image_url TEXT
);

-- Create places table
CREATE TABLE places (
    id TEXT PRIMARY KEY,
    city_id TEXT NOT NULL,
    name TEXT NOT NULL,
    category TEXT,
    description TEXT,
    opening_hours TEXT,
    ticket_price TEXT,
    latitude REAL,
    longitude REAL,
    image_url TEXT,
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE
);

-- Insert sample cities
INSERT INTO cities (id, name, region, description, image_url) VALUES
('1', 'Algiers', 'North', 'The capital city of Algeria, known for its Ottoman palaces and white buildings overlooking the Mediterranean.', 'https://example.com/algiers.jpg'),
('2', 'Oran', 'Northwest', 'A vibrant port city famous for its Spanish architecture and lively music scene.', 'https://example.com/oran.jpg'),
('3', 'Constantine', 'Northeast', 'The "City of Bridges", perched dramatically above deep gorges.', 'https://example.com/constantine.jpg');

-- Insert sample places
INSERT INTO places (id, city_id, name, category, description, opening_hours, ticket_price, latitude, longitude, image_url) VALUES
('101', '1', 'Kasbah of Algiers', 'Historical', 'A UNESCO-listed medina with narrow winding streets, palaces, and mosques.', '8:00 AM - 6:00 PM', 'Free', 36.785, 3.058, 'https://example.com/kasbah.jpg'),
('102', '1', 'Notre-Dame d Afrique', 'Religious', 'A Catholic basilica with stunning sea views.', '9:00 AM - 5:00 PM', 'Free', 36.799, 3.041, 'https://example.com/notredame.jpg'),
('201', '2', 'Santa Cruz Fort', 'Historical', 'A fortress offering panoramic views of Oran and the bay.', '9:00 AM - 7:00 PM', '150 DZD', 35.705, -0.636, 'https://example.com/santacruz.jpg'),
('301', '3', 'Suspended Bridge', 'Bridge', 'An iconic pedestrian bridge suspended above the Rhumel Gorge.', 'Open 24 hours', 'Free', 36.364, 6.608, 'https://example.com/bridge.jpg'),
('302', '3', 'Emir Abdelkader Mosque', 'Religious', 'One of the largest mosques in Algeria, located in Constantine.', '6:00 AM - 10:00 PM', 'Free', 36.365, 6.615, 'https://example.com/mosque.jpg');

