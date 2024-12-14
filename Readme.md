# Quiz Application

A Django-based web application for taking and managing quizzes. Users can answer multiple-choice questions, view results, and restart the quiz. The admin interface allows easy management of quiz questions and categories.

## Features

- Randomized quiz questions.
- Tracks user answers and shows correctness for each.
- Displays a summary of results after completing the quiz.
- Admin interface to manage questions and categories.

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` for installing Python packages

### Step 1: Clone the repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd canvas-quiz
```

### Step 2: Set up a virtual environment
Create and activate a virtual environment to isolate the project dependencies:

```bash
python -m venv .venv
```

On **Windows**:
```bash
.venv\Scripts\activate
```

On **macOS/Linux**:
```bash
source .venv/bin/activate
```

### Step 3: Install dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Set up the database
Run the following command to apply migrations and set up the database:

```bash
python manage.py migrate
```

### Step 5: Create a superuser (optional)
If you want to access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser account.

### Step 6: Run the development server
Start the server with:

```bash
python manage.py runserver
```

Access the app at http://127.0.0.1:8000 in your browser.

## Usage
* Visit the homepage to start the quiz.
* Answer the quiz questions. After completing the quiz, you'll see the result page showing how many questions you answered correctly.
* You can restart the quiz at any time.
* You can add new questions and categories through the Django admin interface.

## Adding More Questions
To add new questions to the quiz:
1. Log in to the Django admin interface at http://127.0.0.1:8000/admin using the superuser credentials.
2. Navigate to the **Questions** section.
3. Click on **Add Question** to create a new quiz question.
4. Fill in the required fields:
   * **Question Text**: The text of the question.
   * **Option A, Option B, Option C, Option D**: The four possible answers.
   * **Correct Option**: The correct answer choice (A, B, C, or D).
   * **Category**: Choose a category (e.g., Art, Astronomy).
5. Save the question to add it to the database.

The new question will automatically be available in the quiz.

## File Structure

```
canvas-quiz/
├── quiz/                # Main app directory
│   ├── migrations/      # Database migrations
│   ├── templates/       # HTML templates for the app
│   │   ├── quiz/
│   │   │   ├── index.html
│   │   │   ├── question.html
│   │   │   ├── results.html
│   ├── __init__.py
│   ├── admin.py         # Admin interface configuration
│   ├── apps.py
│   ├── models.py        # Models for questions and submissions
│   ├── views.py         # Views to handle the quiz logic
│   ├── urls.py          # URL routing for the app
├── manage.py            # Django project management script
├── requirements.txt     # Python package dependencies
├── db.sqlite3           # SQLite database (generated after migration)
```

## Adding and Deleting Questions

### Adding Questions

To add new questions to the quiz:

1. **Log in to the Django admin interface**:
   - Open the admin panel by navigating to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).
   - Log in using the superuser credentials that were created during setup.

2. **Navigate to the Questions section**:
   - In the admin interface, find the **Questions** section in the left sidebar.

3. **Add a new question**:
   - Click on **Add Question** to create a new quiz question.
   - Fill in the required fields:
     - **Question Text**: The question prompt.
     - **Option A, Option B, Option C, Option D**: The four possible answer choices.
     - **Correct Option**: The correct answer choice (A, B, C, or D).
     - **Category**: Choose a category (e.g., Art, Astronomy).

4. **Save the question**:
   - Click **Save** to add the question to the database.

The new question will be available in the quiz automatically.

### Deleting Questions

To delete an existing question:

1. **Log in to the Django admin interface**:
   - Open the admin panel at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) using your superuser credentials.

2. **Navigate to the Questions section**:
   - In the admin interface, find and click on **Questions** in the left sidebar.

3. **Delete a question**:
   - Find the question you want to delete from the list.
   - Click on the question to open the editing page.
   - At the top of the page, you’ll find the **Delete** button. Click it to delete the question from the database.

4. **Confirm the deletion**:
   - Confirm that you want to delete the question. Once deleted, the question will no longer appear in the quiz.

> **Note**: Be cautious when deleting questions, as this action is permanent and cannot be undone unless you restore the database from a backup.

### Deleting Questions via Django Shell

You can also delete questions directly from the Django shell:

1. **Access the Django shell**:
   - Run the following command to enter the Django shell:
     ```bash
     python manage.py shell
     ```

2. **Import the `Question` model**:
   - Run the following command to import the `Question` model:
     ```python
     from quiz.models import Question
     ```

3. **Delete a specific question**:
   - Find and delete the question by running the following command:
     ```python
     question = Question.objects.get(id=<question_id>)
     question.delete()
     ```

   Replace `<question_id>` with the ID of the question you want to delete.

4. **Confirm the deletion**:
   - The question will be deleted from the database.

This method is useful for advanced users or when you need to perform bulk deletions programmatically.


## License
This project is licensed under the MIT License - see the LICENSE file for details.
