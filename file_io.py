from datetime import datetime


def save_markdown_init_research(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"init_research_report_{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result())
    print(f"Report saved as {filename}")
    


def save_markdown_strat_plan(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"strat_planning_report_{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result())
    print(f"Report saved as {filename}")
    
    
def save_markdown_eth_tech(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"eth_tech_report_{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result())
    print(f"Report saved as {filename}")
    
    
def save_markdown_infra_sol(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"strat_infrastructure_solution_report_{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result())
    print(f"Report saved as {filename}")

    
def save_markdown_perf_metric(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"strat_perf_metric_{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result())
    print(f"Report saved as {filename}")
    
    
def save_markdown_final_presentation(task_output):
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"strat_final_presentation_{today_date}.md"
    # Write the task output to the markdown file
    with open(filename, 'w') as file:
        file.write(task_output.result())
    print(f"Report saved as {filename}")