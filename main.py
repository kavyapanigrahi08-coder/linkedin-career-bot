import sys
from ai_engine import AIEngine
from prompts import get_system_prompt
# Session Memory State
session_memory = {
    "name": "",
    "target_role": "",
    "skills": "",
    "experience": "",
    "education": ""
}
def print_header():
    print("\n" + "="*55)
    print("               LINKEDIN CAREER ASSISTANT")
    print("="*55)
def display_menu():
    print("\n--- MAIN MENU ---")
    print("M. Update Profile Memory (Target Role, Skills, etc.)")
    print("1. Analyze LinkedIn Profile")
    print("2. Improve Headline")
    print("3. Write About Section")
    print("4. Improve Experience")
    print("5. Optimize Project")
    print("6. Recommend Skills")
    print("7. Analyze Job Description")
    print("8. Match Profile to Job")
    print("9. Convert Resume to LinkedIn")
    print("10. Generate Recruiter Message")
    print("11. Generate Connection Request")
    print("12. Create Career Roadmap")
    print("13. Interview Preparation")
    print("14. General Career Question")
    print("0. Exit")
    print("-" * 55)
def update_memory():
    print("\n[ Update Session Memory ] (Leave blank to keep existing)")
    name = input(f"Name [{session_memory['name']}]: ").strip()
    if name: session_memory['name'] = name
    role = input(f"Target Role [{session_memory['target_role']}]: ").strip()
    if role: session_memory['target_role'] = role
    skills = input(f"Skills [{session_memory['skills']}]: ").strip()
    if skills: session_memory['skills'] = skills
    print("\n✅ Memory Updated. The Assistant will use this for context.")
def main():
    print_header()
    print("Initializing Gemini 3.5 Flash-Lite Engine...")
    try:
        engine = AIEngine()
    except ValueError as e:
        print(f"\n[Configuration Error]: {e}")
        sys.exit(1)
        
    while True:
        display_menu()
        choice = input("Select an option: ").strip().upper()
        
        if choice == '0':
            print("\nExiting. Good luck with your career journey!\n")
            break
        elif choice == 'M':
            update_memory()
            continue
        elif choice not in [str(i) for i in range(1, 15)]:
            print("\n[Error] Invalid selection. Please choose a number from 1-14, 'M', or '0'.")
            continue

        # Feature-specific prompts to collect required data
        user_input = ""
        
        if choice == '1':
            user_input = input("\nPaste your current LinkedIn profile text:\n> ").strip()
        elif choice == '4':
            user_input = input("\nPaste your raw job experience or bullet points:\n> ").strip()
        elif choice == '5':
            user_input = input("\nPaste details about your project:\n> ").strip()
        elif choice in ['7', '8', '13']:
            user_input = input("\nPaste the target Job Description:\n> ").strip()
            if not user_input:
                print("\n[Error] A Job Description is strictly required for this feature.")
                continue
        elif choice == '9':
            user_input = input("\nPaste your Resume text:\n> ").strip()
        elif choice == '14':
            user_input = input("\nWhat is your career question?\n> ").strip()
        else:
            # Features 2, 3, 6, 10, 11, 12 rely entirely on session memory.
            user_input = "Please generate this based on my provided memory profile."
            if not session_memory['target_role'] and not session_memory['skills']:
                print("\n[Notice] You haven't updated your memory yet. The AI might ask you for more details.")

        print("\n⏳ Analyzing via Gemini 3.5 Flash-Lite...")
        
        # Build prompt & execute
        system_prompt = get_system_prompt(choice, session_memory)
        response = engine.generate_response(system_prompt, user_input)
        
        print("\n" + "="*55)
        print("                   AI RESPONSE")
        print("="*55 + "\n")
        print(response)
        input("\nPress Enter to return to the Main Menu...")

if __name__ == "__main__":
    # Ensure graceful exit on Ctrl+C
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user. Exiting safely.")
        sys.exit(0)