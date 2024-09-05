# Railway Madad

Railway Madad is a platform designed to enhance the complaint resolution process for railway passengers. It allows users to report issues and seek assistance during train journeys by submitting photos, videos, and descriptions of problems. The system categorizes complaints into various types and stores them for efficient handling.

## Features

- **Issue Reporting:** Passengers can report problems related to food, toilets, electrical issues, and emergencies.
- **Multimedia Support:** Users can attach images and videos to their complaints.
- **Categorization:** Automatically categorizes issues into Food Problems, Toilets Problems, Electrical Problems, and Emergency Problems.
- **Efficient Handling:** Prioritizes emergency issues for quicker resolution.

## Installation

To set up Rail Madad on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone git remote add origin https://github.com/BHARATHKUMARREDDY2004/Railway-Madad.git
   cd Railway Madad
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**

   Start the application by running the following command:

   ```bash
   python main.py
   ```

2. **Interact with the System:**

   - **Report a Problem:** Provide details about the issue including train number, coach number, and a description. Attach any relevant images or videos.
   - **Handling Queries:** If your query is unrelated to railway issues, you will be informed that only railway-related problems can be assisted.

3. **Viewing Complaints:**

   Complaints are stored in the `Problems` dictionary categorized as follows:

   - **Food Problems**
   - **Cleanines Problems**
   - **Electrical Problems**
   - **Emergency Problems**

## Contribution

Contributions to Rail Madad are welcome! If you find any issues or have suggestions for improvements, please create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact:

- **Email:** vemireddybharathreddy90@gmaii.com
- **GitHub:** [BHARATHKUMARREDDY2004](https://github.com/BHARATHKUMARREDDY2004)
