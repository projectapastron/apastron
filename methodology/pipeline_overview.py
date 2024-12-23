class PipelineOverview:
    def __init__(self):
        self.steps = [
            "Data Ingestion",
            "Text Preprocessing",
            "Sentiment Analysis",
            "Keyword Extraction",
            "Trend Analysis",
            "Result Compilation"
        ]

    def run_pipeline(self, article):
        """Simulate the entire AI pipeline on an article."""
        processed_article = {
            "step_1": "Ingested",
            "step_2": "Text Processed",
            "step_3": "Sentiment Analyzed",
            "step_4": "Keywords Extracted",
            "step_5": "Trend Calculated",
            "step_6": "Analysis Complete"
        }
        return processed_article

    def describe_pipeline(self):
        """Return a breakdown of the analysis pipeline steps."""
        return {
            "Data Ingestion": "Collects articles from APIs and news sites.",
            "Text Preprocessing": "Cleans and tokenizes text for analysis.",
            "Sentiment Analysis": "Evaluates sentiment (positive/negative/neutral).",
            "Keyword Extraction": "Identifies key terms relevant to crypto trends.",
            "Trend Analysis": "Correlates extracted data with current market trends.",
            "Result Compilation": "Compiles the findings into user-friendly reports."
        }
    
if __name__ == "__main__":
    pipeline = PipelineOverview()
    description = pipeline.describe_pipeline()
    for step, detail in description.items():
        print(f"{step}: {detail}")