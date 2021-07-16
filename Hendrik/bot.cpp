#include <SFML/Graphics.hpp>
#include <math.h>
#include <iostream>
#include <random>
#include "bot.hpp"

Bot::Bot(Game * game) {
	this->game = game;
	this->rotateSpeed = 2.f;
	this->moveSpeed = 3.f;

	/* bot shape */
	//this->shape = sf::CircleShape(30.f, 7);
	this->shape.setRadius(30.f);
	this->shape.setOutlineColor(BOT_OUTLINE_COLOR);
	this->shape.setFillColor(BOT_FILL_COLOR);
	this->shape.setOutlineThickness(5.f);
	this->shape.setOrigin(sf::Vector2f(this->shape.getRadius(), this->shape.getRadius()));
	this->shape.setPosition(sf::Vector2f(this->game->window.getSize().x / 2, this->game->window.getSize().y / 2));

	/* bot direction pointer */
	this->point = sf::CircleShape(5.f, 3);
	this->point.setFillColor(sf::Color::White);
	this->point.setOrigin(sf::Vector2f(this->point.getRadius(), this->shape.getRadius() - this->point.getRadius()));
	this->point.setPosition(this->shape.getPosition());

	/* bot sensors */
	sf::RectangleShape sensor;
	sensor.setSize(sf::Vector2f(4.f, 4.f));
	sensor.setFillColor(BOT_SENSOR_COLOR);
	sensor.setPosition(this->shape.getPosition());
	sensor.setOrigin(sf::Vector2f(SENSOR_OFFSET + sensor.getSize().x, this->shape.getRadius()));
	this->currentPos = sensor.getPosition();
	this->sensors.push_back(sensor);
	sensor.setOrigin(sf::Vector2f(-SENSOR_OFFSET, this->shape.getRadius()));
	this->sensors.push_back(sensor);

	this->shadeBlock.setRadius(30.f);
	this->shadeBlock.setFillColor(SHADE_COLOR);
	this->shadeBlock.setOrigin(sf::Vector2f(this->shadeBlock.getRadius(), this->shadeBlock.getRadius()));
}

void Bot::update(const float dt) {
	/*this->currentTime += dt;
	if (this->currentTime >= SENSOR_INT) {
		this->sense();
		this->currentTime = 0.f;
	}*/
}

void Bot::draw(const float dt) {
	for (auto block : this->shade) this->game->window.draw(block);
	for (auto obstacle : this->obstacles) this->game->window.draw(obstacle.shape);
	this->game->window.draw(this->shape);
	this->game->window.draw(this->point);
	for (auto sensor : this->sensors) this->game->window.draw(sensor);
}

void Bot::rotate(const int dir) {
	float noise = normal(gen);
	this->shape.rotate(dir * (this->rotateSpeed + noise));
	this->point.rotate(dir * (this->rotateSpeed + noise));
	for (int i = 0; i < this->sensors.size(); i++) this->sensors[i].rotate(dir * (this->rotateSpeed + noise));
	this->sense();
}

void Bot::move(const int dir) {
	sf::Vector2f originalPos = this->shape.getPosition();
	float noise = normal(gen) / this->moveSpeed;
	float x = dir * (this->moveSpeed + noise) * (sin(-M_PI * this->shape.getRotation() / 180.f));
	float y = dir * (this->moveSpeed + noise) * (cos(-M_PI * this->shape.getRotation() / 180.f));
	this->shape.move(sf::Vector2f(x, y));
	this->point.move(sf::Vector2f(x, y));
	for (int i = 0; i < this->sensors.size(); i++) this->sensors[i].move(sf::Vector2f(x, y));

	/* check for collisions */
	for (auto wall : this->game->walls) {
		if (this->intersect(this->shape, wall)) {
			this->shape.setPosition(originalPos);
			this->point.setPosition(originalPos);
			for (int i = 0; i < this->sensors.size(); i++) this->sensors[i].setPosition(originalPos);
			break;
		}
	}	

	/* add shade */
	bool add = true;
	for (auto block : shade) {
		if (pow(block.getPosition().x - originalPos.x, 2) < 100.f && pow(block.getPosition().y - originalPos.y, 2) < 100.f) {
			add = false;
			break;
		}
	}
	if (add) {
		this->shadeBlock.setPosition(originalPos);
		this->shade.push_back(this->shadeBlock);
	}
	if (sqrt(pow(originalPos.x - this->currentPos.x, 2) + pow(originalPos.y - this->currentPos.y, 2)) >= 10.f) this->sense();
}

void Bot::sense() {
	/* acquire minimum points */
	std::vector<sf::RectangleShape> obstacles = this->getViewObstacles();
	std::vector<float> minS1(SENSOR_SAMPLES, 10000);
	std::vector<float> minS2(SENSOR_SAMPLES, 10000);
	sf::Vector2f pos1 = this->sensors[0].getTransform().transformPoint(sf::Vector2f(0, 0));
	sf::Vector2f pos2 = this->sensors[1].getTransform().transformPoint(sf::Vector2f(0, 0));

	for (auto obstacle : obstacles) {
		std::vector<float> distance1v;
		std::vector<float> distance2v;

		distance1v.push_back(2 * sqrt(pow(obstacle.getPosition().x - pos1.x, 2) + pow(obstacle.getPosition().y - pos1.y, 2)));
		distance1v.push_back(2 * sqrt(pow(obstacle.getPosition().x + obstacle.getSize().x - pos1.x, 2) + pow(obstacle.getPosition().y - pos1.y, 2)));
		distance1v.push_back(2 * sqrt(pow(obstacle.getPosition().x - pos1.x, 2) + pow(obstacle.getPosition().y + obstacle.getSize().y - pos1.y, 2)));
		distance1v.push_back(2 * sqrt(pow(obstacle.getPosition().x + obstacle.getSize().x - pos2.x, 2) + pow(obstacle.getPosition().y + obstacle.getSize().y - pos1.y, 2)));
		distance2v.push_back(distance1v[0] / 2.f + sqrt(pow(obstacle.getPosition().x - pos2.x, 2) + pow(obstacle.getPosition().y - pos2.y, 2)));
		distance2v.push_back(distance1v[1] / 2.f + sqrt(pow(obstacle.getPosition().x + obstacle.getSize().x - pos2.x, 2) + pow(obstacle.getPosition().y - pos2.y, 2)));
		distance2v.push_back(distance1v[2] / 2.f + sqrt(pow(obstacle.getPosition().x - pos2.x, 2) + pow(obstacle.getPosition().y + obstacle.getSize().y - pos2.y, 2)));
		distance2v.push_back(distance1v[3] / 2.f + sqrt(pow(obstacle.getPosition().x + obstacle.getSize().x - pos1.x, 2) + pow(obstacle.getPosition().y + obstacle.getSize().y - pos2.y, 2)));
		
		std::sort(distance1v.begin(), distance1v.end());
		std::sort(distance2v.begin(), distance2v.end());
		int index1 = 0, index2 = 0;

		for (size_t i = 0; i < SENSOR_SAMPLES; i++) {
			if (minS1[i] > distance1v[index1]) {
				minS1[i] = distance1v[index1];
				if (index1 < distance1v.size() - 1) index1++;
				else break;
			}
		}
		for (size_t i = 0; i < SENSOR_SAMPLES; i++) {
			if (minS2[i] > distance2v[index2]) {
				minS2[i] = distance2v[index2];
				if (index2 < distance2v.size() - 1) index2++;
				else break;
			}
		}
	}
	std::sort(minS1.begin(), minS1.end());
	std::sort(minS2.begin(), minS2.end());
	for (size_t i = 0; i < minS1.size(); i++) {
		if (minS1[i] > SENSOR_MAX) {
			minS1.erase(minS1.begin() + i, minS1.end());
			break;
		}
	}
	for (size_t i = 0; i < minS2.size(); i++) {
		if (minS2[i] > SENSOR_MAX) {
			minS2.erase(minS2.begin() + i, minS2.end());
			break;
		}
	}

	/* calculate possible positions */
	//this->obstacles.clear();
	if (minS1.size() > 0 && minS2.size() > 0) {
		std::vector<sf::Vector2f> locations = this->ellipticLocalization(minS1, minS2);
		this->updatePerceivedObstacles(locations);
	}
}

bool Bot::intersect(sf::CircleShape bot, sf::RectangleShape wall) {
	/* get vector distances */
	sf::Vector2f vDistances[4];
	vDistances[0] = sf::Vector2f(wall.getPosition().x - bot.getPosition().x, wall.getPosition().y - bot.getPosition().y);
	vDistances[1] = sf::Vector2f(wall.getPosition().x + wall.getSize().x - bot.getPosition().x, wall.getPosition().y - bot.getPosition().y);
	vDistances[2] = sf::Vector2f(wall.getPosition().x - bot.getPosition().x, wall.getPosition().y + wall.getSize().y - bot.getPosition().y);
	vDistances[3] = sf::Vector2f(wall.getPosition().x + wall.getSize().x - bot.getPosition().x, wall.getPosition().y + wall.getSize().y - bot.getPosition().y);

	/* convert to absolute distance */
	float distances[4];
	float sum;
	for (size_t i = 0; i < 4; i++) {
		distances[i] = sqrt(pow(vDistances[i].x, 2) + pow(vDistances[i].y, 2));
		if (distances[i] <= bot.getRadius()) return true;
		sum += distances[i];
	}
	if (sum / 4.f < wall.getSize().x) return true;
	
	return false;
}

std::vector<sf::RectangleShape> Bot::getViewObstacles() {
	float angle1 = (this->shape.getRotation() - SENSOR_ANGLE) * M_PI / 180.f;
	float angle2 = (this->shape.getRotation() + SENSOR_ANGLE) * M_PI / 180.f;
	if (angle1 > M_PI) angle1 -= 2 * M_PI;
	if (angle2 > M_PI) angle2 -= 2 * M_PI;
	sf::Vector2f pos = this->shape.getPosition();
	std::vector<sf::RectangleShape> viewObstacles;

	for (size_t i = 0; i < this->game->walls.size(); i++) {
		sf::RectangleShape * wall = &this->game->walls[i];
		wall->setFillColor(WALL_COLOR);
		float angle = atan2(wall->getPosition().y - pos.y, wall->getPosition().x - pos.x) + M_PI / 2.f;
		if (angle > M_PI) angle -= 2 * M_PI;
		if ((angle1 < angle2 && angle >= angle1 && angle <= angle2) ||
			(angle1 > angle2 && (angle >= angle1 || angle <= angle2))) {
			wall->setFillColor(WALL_SENSE_COLOR);
			viewObstacles.push_back(*wall);
		}
	}

	return viewObstacles;
}

void Bot::updatePerceivedObstacles(std::vector<sf::Vector2f> locations) {
	float angle1 = (this->shape.getRotation() - SENSOR_ANGLE) * M_PI / 180.f;
	float angle2 = (this->shape.getRotation() + SENSOR_ANGLE) * M_PI / 180.f;
	if (angle1 > M_PI) angle1 -= 2 * M_PI;
	if (angle2 > M_PI) angle2 -= 2 * M_PI;
	sf::Vector2f pos = this->shape.getPosition();
	std::vector<Obstacle *> viewObstacles;

	for (size_t i = 0; i < this->obstacles.size(); i++) {
		Obstacle * obstacle = &this->obstacles[i];
		float angle = atan2(obstacle->shape.getPosition().y - pos.y, obstacle->shape.getPosition().x - pos.x) + M_PI / 2.f;
		if (angle > M_PI) angle -= 2 * M_PI;
		if ((angle1 < angle2 && angle >= angle1 && angle <= angle2) ||
			(angle1 > angle2 && (angle >= angle1 || angle <= angle2))) {
			obstacle->found = false;
			obstacle->index = i;
			obstacle->distance = sqrt(pow(obstacle->shape.getPosition().x - this->shape.getPosition().x, 2) + pow(obstacle->shape.getPosition().y - this->shape.getPosition().y, 2));
			viewObstacles.push_back(obstacle);
		}
	}

	for (auto location : locations) {
		bool found = false;
		for (size_t i = 0; i < viewObstacles.size(); i++) {
			float distance = sqrt(pow(viewObstacles[i]->shape.getPosition().x - location.x, 2) + pow(viewObstacles[i]->shape.getPosition().y - location.y, 2));
			if (distance <= OBSTACLE_MAX_DIST) {
				viewObstacles[i]->lives++;
				viewObstacles[i]->found = true;
				found = true;
				break;
			}
		}
		if (!found) this->obstacles.push_back(Obstacle(location));
	}

	for (size_t i = 0; i < viewObstacles.size(); i++) {
		if (!viewObstacles[i]->found) viewObstacles[i]->lives--;
		if (viewObstacles[i]->lives <= 0) this->obstacles.erase(this->obstacles.begin() + viewObstacles[i]->index);
	}
}

std::vector<sf::Vector2f> Bot::ellipticLocalization(std::vector<float> r1, std::vector<float> r2) {
	std::vector<sf::Vector2f> output;
	float angle = (this->shape.getRotation() - 90.f) * M_PI / 180.f;
	sf::Transform pos = this->sensors[0].getTransform();

	for (size_t i = 0; i < r1.size(); i++) {
		for (size_t j = 0; j < r2.size(); j++) {
			float newX = (r1[i] * r2[j] - pow(r2[j], 2)) / (4 * SENSOR_OFFSET);
			float newY = (sqrt(pow(r2[j], 2) - pow(2 * SENSOR_OFFSET, 2)) * sqrt(pow(2 * SENSOR_OFFSET, 2) - pow(r1[i] - r2[j], 2))) / (4 * SENSOR_OFFSET);
			if (!isnan(newX) && !isnan(newY)) {
				std::cout << newX << ", " << newY << std::endl;
				output.push_back(pos.transformPoint(sf::Vector2f(newX, -newY)) - this->sensors[0].getSize());
			}
		}
	}
	//if (output.size() > 0) std::cout << output[0].x << ", " << output[0].y << std::endl;
	return output;
}