from project import User, Articles, Patterns, Problems

# Run tests with: python3 -m pytest

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(user_name='testUser', email='testUser@test.com')
    assert user.email == 'testUser@test.com'
    assert user.password == 'placeholder'
    assert user.active == 1

def test_articles():
    article = Articles(article_name="test_article_name", article_link = "test_article_link.com", pattern_id=1)

    assert article.article_name == "test_article_name"
    assert article.article_link == "test_article_link.com"
    assert article.pattern_id == 1

def test_patterns():
    pattern = Patterns(pattern_name="test_pattern_name")

    assert pattern.pattern_name == "test_pattern_name"

def test_problems():
    problem = Problems(problem_name="test_problem_name", problem_link="test_leetcode.com/problem_id", pattern_id=1, difficulty_level=1)

    assert problem.problem_name == "test_problem_name"
    assert problem.problem_link == "test_leetcode.com/problem_id"
    assert problem.pattern_id == 1
    assert problem.difficulty_level == 1
