-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
  IN user_id INT
)
BEGIN
  DECLARE total_score FLOAT DEFAULT 0;
  DECLARE total_weight INT DEFAULT 0;
  
  SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
  INTO total_score, total_weight
  FROM corrections
  INNER JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;
  
  IF total_weight > 0 THEN
    SET total_score = total_score / total_weight;
  END IF;
  
  UPDATE users
  SET average_score = total_score
  WHERE users.id = user_id;
END;
//
DELIMITER ;
