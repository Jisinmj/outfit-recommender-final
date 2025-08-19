import pandas as pd

# Load wardrobe CSV
wardrobe = pd.read_csv("data/wardrobe.csv")

def recommend_outfit(weather: str, occasion: str):
    """
    Recommend outfits based on weather and occasion.
    """
    filtered = wardrobe[
        (wardrobe["occasion"] == occasion) &
        (wardrobe["temperature_range"] == weather)
    ]
    if filtered.empty:
        return "❌ Sorry, no matching outfit found."
    return filtered[["type", "color"]].to_dict(orient="records")

if __name__ == "__main__":
    print("✨ Outfit Recommender ✨")
    w = input("Enter weather (hot/moderate/cold): ").strip().lower()
    o = input("Enter occasion (casual/formal): ").strip().lower()
    print("👕 Suggested outfits:", recommend_outfit(w, o))

