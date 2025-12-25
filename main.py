from app.pipeline import run_pipeline

def main():
    try:
        url = input("Enter YouTube URL: ")
        summary = run_pipeline(url)
        print("\n===== FINAL SUMMARY =====\n")
        print(summary)

    except Exception as e:
        print("Something went wrong:", e)

if __name__ == "__main__":
    main()
