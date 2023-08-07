script_path="$(dirname "$0")"
cd "$script_path"

cat extra_social.txt dating.txt tiktok.txt | sort | uniq > social.txt
python3 ../convert_adblock.py social.txt
