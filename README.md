# Every Wataten Frame In Order

<img src="wataten.jpeg" width="150px" align="right" />

This code utilizes moviepy and pillow to automatically post Every Wataten frame to a Telegram group. Please note that this program only posts photos to a Telegram group or channel, and it does not support posting to platforms like Facebook (I have a skill issue in setting up configuration to the meta API).



# Setup Instructions
1. Clone this project with
    ```bash
    git clone https://github.com/miruchigawa/every-frame-in-order
    ```
2. Install all required dependencies
    ```bash
    pip install -r REQUIREMENTS.txt
    ```
3. Copy `config.py.example` to `config.py` and fill in the necessary data.
4. Find the `chat_id` by visiting
    ```url
    https://api.telegram.org/bot{telegram_key}/getUpdates
    ```
5. If no chat_id is found, try sending a message and check again.

6. Run the program
    ```bash
    python3 main.py
    ```

# Todo
- [ ] Support for rating branches/votes
- [ ] Automatic cron job
- [x] Support channel