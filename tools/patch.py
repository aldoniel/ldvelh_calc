import tomllib

# Define file paths
text_file_path = "ldvelh_gui_editor.py"  # The text file containing incorrect sentences
toml_file_path = "corrections.toml"  # The TOML file with corrections
output_file_path = "ldvelh_gui.py"  # The new file with corrected text
if text_file_path == output_file_path:
    raise ValueError("entrée == sortie") 

# Read the TOML corrections file
with open(toml_file_path, "rb") as toml_file:  # tomllib requires binary mode
    corrections = tomllib.load(toml_file)

# Read the text file
with open(text_file_path, "r", encoding="utf-8") as text_file:
    text_content = text_file.read()

# Track missing sentences
missing_sentences = []
doublons:list=[]
count:int=0

# Apply corrections
for entry in corrections["corrections"]["entries"]:
    incorrect_sentence = entry["er"]
    correct_sentence = entry["cr"]
    
    if incorrect_sentence in text_content:
        count = text_content.count(incorrect_sentence)
        if count>1:
            doublons.append(incorrect_sentence)
        text_content = text_content.replace(incorrect_sentence, correct_sentence,1)
    else:
        missing_sentences.append(incorrect_sentence)

# If there are missing sentences, raise an exception and log the errors
if  doublons:
    print("Error: doublons:\n" + "\n".join(doublons))
    raise ValueError("la ligne remplacée doit être unique" )
    
if missing_sentences:
    error_message = "Error: The following sentences were not found in the text file:\n" + "\n".join(missing_sentences)
    print(error_message)
    raise ValueError("Some incorrect sentences were not found in the text. Check your input file.")

# Write the corrected text to a new file
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(text_content)

print("Corrections applied successfully! Saved to", output_file_path)
