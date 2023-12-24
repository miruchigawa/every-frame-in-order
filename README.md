# Every Wataten Frame In Order

<img src="wataten.jpeg" width="150px" align="right" />

This code utilizes MoviePy and Pillow to automatically post every Wataten frame to a Telegram group or Facebook page. ~~Please note that this program only posts photos to a Telegram group or channel, and it now supports posting to platforms like Facebook (previously, there was a skill issue in setting up configuration to the meta API).~~ Now supported both

[日本語](ja.md)

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
- [x] Added supported Facebook method

If you have any questions, please chat with me on Facebook: [me](https://www.facebook.com/mirudev.jp)