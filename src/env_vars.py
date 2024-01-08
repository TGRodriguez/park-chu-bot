from dotenv import load_dotenv
import argparse


def load_env_vars():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", help="Run in development mode", action="store_true")
    args = parser.parse_args()
    if args.dev:
        load_dotenv()
