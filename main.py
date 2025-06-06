
def main():
    print("ByteMeAI is starting...")
    load_env()
    model = load_model()

    while True:
        viewer_input = input("Viewer message: ")
        if viewer_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        reply = generate_response(viewer_input, model)
        print(f"ByteMeAI: {reply}\n")

if __name__ == "__main__":
    main()
def main():
    print("ByteMeAI is starting...")
    load_env()
    model = load_model()

    while True:
        viewer_input = input("Viewer message: ")
        if viewer_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        reply = generate_response(viewer_input, model)
        print(f"ByteMeAI: {reply}\n")

if __name__ == "__main__":
    main()
