from dotenv import load_dotenv
load_dotenv()
from file_io import save_markdown_init_research, save_markdown_strat_plan, save_markdown_eth_tech, save_markdown_infra_sol, save_markdown_perf_metric,  save_markdown_final_presentation
from crewai import Crew,Process,Task,Agent

from tasks import AiConsultantTasks
from agents import AiConsultantAgents

tasks = AiConsultantTasks()
agents = AiConsultantAgents()

import sys

# Inputs from command line
company = input('Enter Company Name: ')
industry = input('Enter Industry: ')
niche = input('Enter Niche: ')
website = input('Enter website: ')

# Choices
options = [
    'Enhancing Customer Experience',
    'Optimizing Operational Efficiency',
    'Driving Innovation in Products/Services',
    'Improving Marketing and Sales Strategies'
]

# Display choices
print("\nSelect an AI Solution:")
for idx, option in enumerate(options, 1):
    print(f"{idx}. {option}")

# Get user choice
choice_index = int(input("Enter the number of your choice (1-4): "))
if 1 <= choice_index <= 4:
    choice = options[choice_index - 1]

# Display selected information
if 'choice' in locals():
    print(f'\nCompany Name: {company}')
    print(f'Industry: {industry}')
    print(f'Niche: {niche}')
    print(f'Niche: {website}')
    print(f'Selected AI Solution: {choice}')
# context = f"Building AI Strategy for the {company} working in the industry {industry} specialy in the niche {niche} "



# Create Agents
data_researcher_agent = agents.Information_and_Data_Researcher()
organizational_management_agent = agents.Organizational_Management_Consultant()
business_analyst_agent = agents.Business_Analyst_for_AI()
competitive_inteligence_analyst_agent = agents.Competitive_Intelligence_Analyst()
ai_solutions_architect_agent = agents.AI_Solutions_Architect()
ai_infrastructure_specialist_agent = agents.AI_Infrastructure_Specialist()
ethic_compliance_agent = agents.AI_Ethics_and_Compliance_Officer()
project_manager_agent = agents.Project_Manager_for_AI_Projects()
ai_project_editor = agents.AI_Report_Editor()

# Create tasks
# I - Phase : Initial research and analysis:
company_analysis_task = tasks.Company_Analysis_Task(data_researcher_agent, industry, niche, company, website)
industry_niche_analysis_task = tasks.Industry_and_Niche_Analysis_Task(data_researcher_agent, industry, niche, company)
market_competitive_analysis_task = tasks.Market_Competitive_AI_Landscape_Analysis_Task(competitive_inteligence_analyst_agent, industry, niche)
organizational_analysis_task = tasks.Organizational_AI_Readiness_Assessment_Task(organizational_management_agent, company, industry, website)
initial_research_and_analysis_report = tasks.Initial_Research_and_Analysis_Report(ai_project_editor,industry, niche, company,website,save_markdown_init_research )

# II - Phase : Strategy planning:
goal_alignement_strategy_task = tasks.Goal_Alignment_Strategy_Definition_Task(business_analyst_agent, choice)
strategy_planning_report_task = tasks.Strategic_Planning_Report(ai_project_editor, save_markdown_strat_plan)

# III - Phase : ethical and technical analysis
ethic_analysis_task = tasks.AI_Ethical_Compliance_Guidelines_Formulation_Task(ethic_compliance_agent, industry, niche)
ai_technical_analysis_task = tasks.AI_Technical_Feasibility_Impact_Analysis_Task(ai_solutions_architect_agent, company, industry, niche, choice, website)
ethical_and_technical_analysis_report = tasks.Ethical_and_Technical_Analysis_Report(ai_project_editor,save_markdown_eth_tech)

# IV - infrastructure and solution design
infrastructure_design_task = tasks.Infrastructure_Design_Optimization_Plan_Task(ai_infrastructure_specialist_agent, industry, niche, choice, website)
solution_design_task = tasks.AI_Solution_Design_Development_Plan_Task(ai_solutions_architect_agent, company, industry, niche, choice, website)
infrastructure_and_solution_design_report = tasks.Infrastructure_and_Solution_Design_Report(ai_project_editor,save_markdown_infra_sol )

# V - Performance Metrics and ROI Analysis
define_performance_metrics_task = tasks.Define_Performance_Metrics_Task(business_analyst_agent, company)
conduct_roi_analysis_task = tasks.Conduct_ROI_Analysis_Task(business_analyst_agent)
prioritize_ai_initiative = tasks.Prioritize_AI_Initiatives_Task(project_manager_agent)
performance_metrics_and_roi_analysis_report = tasks.performance_metrics_and_ROI_analysis_report_task(ai_project_editor, company, save_markdown_perf_metric)

# VI - Project framework 
project_management_framework_task = tasks.AI_Project_Management_Coordination_Framework_Task(project_manager_agent, company, industry, niche, choice, website)

# VII - Final report
final_presentation_report = tasks.Final_Presentation_Report(ai_project_editor, save_markdown_final_presentation )


# Create Crew responsible 

crew_ai_consultant = Crew(
	agents=[
		data_researcher_agent,
		competitive_inteligence_analyst_agent,
		organizational_management_agent,
		ai_project_editor,
        business_analyst_agent,
        ethic_compliance_agent,
        ai_solutions_architect_agent,
        ai_infrastructure_specialist_agent,
        project_manager_agent
	],
 
	tasks=[
		company_analysis_task,
		industry_niche_analysis_task,
		market_competitive_analysis_task,
		organizational_analysis_task,
        initial_research_and_analysis_report,
        goal_alignement_strategy_task,
        strategy_planning_report_task,
        ethic_analysis_task,
        ai_technical_analysis_task,
        ethical_and_technical_analysis_report,
        infrastructure_design_task,
        solution_design_task,
        infrastructure_and_solution_design_report,
        define_performance_metrics_task,
        conduct_roi_analysis_task,
        prioritize_ai_initiative,
        performance_metrics_and_roi_analysis_report,
        project_management_framework_task,
        final_presentation_report
	],
    Process= Process.sequential,
    full_output=True,
    verbose=True,
)

ai_research_report = crew_ai_consultant.kickoff()


# Print results
print("\n\n################################################")
print("## Here is you final report")
print("################################################\n")
print(ai_research_report)
