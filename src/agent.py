# Agent Orchestrator

import data_loader
import analysis_tool
import recommendation_engine

class InvestmentAgent:
    def __init__(self):
        self.data = None
        self.analysis_results = None
        self.recommendations = None

    def load_data(self):
        self.data = data_loader.load_data()

    def analyze_data(self):
        self.analysis_results = analysis_tool.perform_analysis(self.data)

    def generate_recommendations(self):
        self.recommendations = recommendation_engine.generate_recommendations(self.analysis_results)

    def run(self):
        self.load_data()
        self.analyze_data()
        self.generate_recommendations()
        return self.recommendations

if __name__ == '__main__':
    agent = InvestmentAgent()
    recommendations = agent.run()
    print(recommendations)