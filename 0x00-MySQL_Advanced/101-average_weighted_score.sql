-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users u
  INNER JOIN (
    SELECT user_id, SUM(corrections.score * projects.weight) AS total_score, SUM(projects.weight) AS total_weight
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    GROUP BY user_id
  ) AS weighted_scores ON u.id = weighted_scores.user_id
  SET u.average_score = CASE WHEN weighted_scores.total_weight > 0 THEN weighted_scores.total_score / weighted_scores.total_weight ELSE 0 END;
END;
//
DELIMITER ;
