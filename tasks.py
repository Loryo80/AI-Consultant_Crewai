from crewai import Task
from textwrap import dedent

class AiConsultantTasks():
    # I - Phase : Initial research and analysis:
    def Company_Analysis_Task(self, agent,industry, niche, company, website):
        return Task(
            description=f"""\
                Focus this task on gathering comprehensive data about the {company}'s history, market position in {niche}, strengths, weaknesses, 
                opportunities, and threats (SWOT analysis) to provide a foundational understanding for strategic planning in the {industry} and specialy in the {niche}.
                use the website {website} to gather more information.
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}  
                """,
            expected_output="""\
                A detailed report on {company} analyzing its industry position, market share, financial performance, key competitors, 
                and recent developments. The report should provide actionable insights that contribute to the initial research 
                and analysis phase of the AI consultation project.
                Selected company by the customer: {company}""",
            async_execution=False,
            agent=agent
        )
    
    def Industry_and_Niche_Analysis_Task(self, agent, industry, niche, company):
        return Task(
            description=dedent(f"""\
                Conduct a comprehensive analysis of the {industry} industry, with a focus on the {niche} niche. This includes:

                1. Market Trends: Identifying current trends, challenges, and opportunities within the industry and niche.
                2. Competitor Analysis: Analyzing  {company}'s competitors' strategies, strengths, weaknesses, and potential AI adoption.
                3. Regulatory Landscape: Understanding relevant regulations and compliance requirements affecting AI implementation.
                4. Potential Use Cases: Identifying potential AI applications and use cases specific to the industry and niche.

                The analysis will provide valuable insights for tailoring AI solutions to meet the unique needs of the client.
                
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}"""),
            expected_output="A comprehensive analysis report on the {industry} industry and {niche} niche, highlighting market trends, competitor insights, regulatory considerations, and potential AI use cases.",
            async_execution=False,
            agent=agent
        )

    def Market_Competitive_AI_Landscape_Analysis_Task(self, agent, industry, niche):
        return Task(
            description=dedent(f"""\
                Perform a comprehensive analysis of the competitive landscape and market trends in the {industry} industry, particularly within the {niche} niche. This task includes:

                1. Competitive Analysis: Identify key competitors and their AI strategies, strengths, and weaknesses within the {niche} niche.
                2. Market Trends: Analyze current market trends affecting AI adoption in the {industry}, with a focus on how these trends could impact {niche}.
                3. Opportunity Identification: Highlight opportunities for differentiation and innovation in AI applications that can give a competitive edge.

                This analysis will inform the strategic positioning and AI solution development for companies within this niche, ensuring a competitive advantage.
                
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}"""),
            expected_output=dedent("""\
                A report on the competitive landscape and market trends within the {industry} industry and {niche} niche, including 
                competitor strategies, market trends, and identified opportunities for differentiation and innovation in AI. The report 
                should offer actionable intelligence for strategic decision-making."""),
            async_execution = False,
            agent= agent
        )

    def Organizational_AI_Readiness_Assessment_Task(self, agent, company, industry, website):
        return Task(
            description=dedent(f"""\
                Conduct an assessment of {company}'s readiness for AI integration, focusing on the {industry} sector.
                use the website {website} to gather more information.
                Evaluate:

                1. Current Infrastructure: Assess the existing IT and data infrastructure's capability to support AI technologies.
                2. Organizational Structure: Analyze the organizational structure for potential barriers to AI adoption and recommend changes.
                3. Skillset Evaluation: Identify skill gaps in the current workforce and suggest training programs or hiring strategies.
                4. Cultural Readiness: Gauge the organizational culture's openness to AI-driven change and propose initiatives to foster AI readiness.

                The objective is to create a comprehensive overview of {company}'s preparedness for embracing AI, identifying areas of strength and opportunities for improvement.
                
                Selected website by the customer: {website}
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}"""),
            expected_output=dedent("""\
                An AI readiness report for {company}, covering infrastructure, organizational structure, workforce skills, 
                and cultural readiness. The report will outline strengths, gaps, and recommendations to prepare {company} 
                for successful AI adoption."""),
            async_execution=False,
            agent=agent
        )
   
    def Initial_Research_and_Analysis_Report(self, agent, industry, niche, company, website, callback_function):
        return Task(
            description=dedent("""\
                Compile the findings of the initial research and analysis conducted in the company_analysis_task,industry_niche_analysis_task,market_competitive_analysis_task, 
                organizational_analysis_task. to consolidate the insights from the initial research phases into a strategic report that directly addresses how emerging trends, competitive dynamics, and market opportunities can be leveraged or navigated to enhance the {company}'s positioning within its {niche} and {industry}. The report will:

                1. {Industry} Dynamics: Delve into current and upcoming trends in the {industry}, evaluating their implications for the company's operational and strategic direction. This includes assessing technological advancements, regulatory changes, and market shifts.

                2. {niche}-Specific Insights: Offer a deep dive into the {company}'s specific {niche}, identifying unique opportunities for differentiation and potential {niche}-specific challenges.

                3. Competitive Positioning: Analyze the competitive landscape with a focus on direct competitors and emerging players, assessing their strategies, strengths, weaknesses, and potential threats or opportunities for the company.

                4. Strategic Opportunities and Risks: Highlight specific areas where AI can be strategically applied to seize opportunities or mitigate risks, tailored to the company's unique context within its {industry} and niche.

                The goal is to provide actionable intelligence that will guide the {company} in making informed strategic decisions, prioritizing AI initiatives that offer the most significant potential for competitive advantage and growth.

                use the website {website} to gather more information.
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}                
                """),
            expected_output=dedent("""\
                 A strategic report that offers a cohesive and comprehensive analysis tailored to the {company}'s context, focusing on actionable insights for AI implementation. 
                 in markdown format, with a consistent style and layout,Key components of the report should include:

                - A nuanced understanding of {industry} and {niche}-specific trends, and their potential impacts on the {company}.
                - A critical assessment of the competitive landscape, with strategic recommendations for positioning the {company} effectively.
                - Clearly identified opportunities for leveraging AI to enhance the {company}'s market position, innovate in its offerings, or streamline operations.
                - A prioritized list of potential AI projects, each accompanied by a preliminary assessment of its impact on the {company}'s strategic goals and market position.

                The report will serve as a critical input for the strategic planning phase, enabling the {company} to focus its AI initiatives where they can deliver the most value.
                Your final report MUST be full super detailed report."""),
            async_execution=False,
            agent=agent,
            callback=callback_function
        )

    # II - Phase : Strategy planning:
    def Goal_Alignment_Strategy_Definition_Task(self, agent, client_choice):
        return Task(
            description=dedent(f"""\
                Align the client's goals with appropriate AI strategies based on their chosen objective: {client_choice}. This involves:

                1. Goal Definition: Clarifying and refining the client's objectives for AI implementation.
                2. Strategy Formulation: Developing tailored AI strategies aligned with the chosen goal.
                3. Resource Identification: Identifying the resources, expertise, and technologies required to execute the strategies.
                4. Risk Assessment: Anticipating potential risks and challenges associated with each strategy and proposing mitigation measures.

                The goal alignment and strategy definition will provide a clear roadmap for leveraging AI to achieve the client's objectives.
                
                Client's selected goal: {client_choice}"""),
            expected_output=dedent(f"""\
                A detailed strategy document aligning the client's goals with specific AI strategies tailored to achieve the objective of {client_choice}. 
                The document will outline key action steps, resource requirements, risk assessments, and timelines for strategy execution."""),
            async_execution=False,
            agent=agent
        )

    def Strategic_Planning_Report(self, agent , callback_function):
        return Task(
            description=dedent("""\
                Develop a strategic planning report based on the alignment of goals and strategy definitions established in the goal_alignement_strategy_task task. This comprehensive report should articulate:

                1. Objectives: Clearly outline the objectives for AI initiatives, ensuring they align with the overall business strategy and goals.
                2. Implementation Plan: Detail the plan for implementing AI solutions, including timelines, technology requirements, necessary talent and resources, and integration with existing systems.
                3. Risk Management Strategies: Identify potential risks associated with the AI initiatives and propose strategies to mitigate these risks, ensuring a resilient approach to implementation.
                4. Performance Metrics: Define metrics and benchmarks to measure the performance and impact of AI initiatives on the business, facilitating ongoing evaluation and adjustments.

                This report should serve as a roadmap, guiding the organization through the complexities of implementing AI solutions, with a clear focus on achieving strategic objectives."""),
            expected_output=dedent("""\
                A detailed strategic planning report in markdown format, with a consistent style and layout.that outlines:
                
                - The objectives for adopting AI within the organization, demonstrating how these initiatives align with broader business goals.
                - A comprehensive implementation plan that includes actionable steps, timelines, and resource requirements, ensuring a structured approach to AI integration.
                - Risk management strategies that address potential challenges and outline measures to mitigate these risks effectively.
                - Performance metrics and benchmarks designed to evaluate the success and impact of AI initiatives on the organization.

                The report should offer actionable recommendations, enabling the organization to proceed with confidence in deploying AI solutions, and establish a framework for measuring success and making data-driven adjustments."""),
            async_execution=False,
            agent=agent,
            callback=callback_function
        )

   # III - Phase : ethical and technical analysis
   
    def AI_Ethical_Compliance_Guidelines_Formulation_Task(self, agent, industry, niche):
        return Task(
            description=dedent(f"""\
                Develop a set of ethical and compliance guidelines for AI deployment within the {industry} industry and {niche} niche. Address:

                1. Data Privacy and Security: Establish guidelines for managing user data ethically and in compliance with relevant regulations.
                2. Bias Mitigation: Outline measures to identify and mitigate biases in AI algorithms and data sets.
                3. Transparency and Accountability: Define standards for maintaining transparency in AI decision-making processes.
                4. Compliance Checklist: Create a compliance checklist specific to {industry} regulations and ethical standards.

                These guidelines will ensure that AI solutions are developed and implemented responsibly, ethically, and in compliance with all regulations and best practices.
                
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}"""),
            expected_output=dedent("""\
                A document outlining ethical guidelines and compliance requirements for AI deployment in the {industry} industry and {niche} niche, 
                including data privacy, bias mitigation, transparency, and a compliance checklist. This will serve as a foundational framework for 
                responsible AI development and deployment."""),
            async_execution=False,
            agent=agent
        )

    def AI_Technical_Feasibility_Impact_Analysis_Task(self, agent, company, industry, niche, client_choice, website):
        return Task(
            description=dedent(f"""\
                Conduct a technical feasibility study and impact analysis for deploying AI within {company} in the {industry} sector, especially focusing on the {niche} niche. This involves:

                1. Technical Requirements: Identifying the technical specifications and requirements for the proposed AI solutions.
                2. Impact Analysis: Assessing the potential impact of AI on existing workflows, employee roles, and overall productivity.
                3. Cost-Benefit Analysis: Performing a cost-benefit analysis to evaluate the financial implications of AI adoption.
                4. Integration Challenges: Identifying potential integration challenges with existing systems and proposing solutions.

                The outcome will be a detailed report that outlines the feasibility, expected benefits, costs, and potential hurdles in integrating AI into {company}'s operations to achieve the goal of {client_choice}.
                
                use the website {website} to gather more information.
                Selected website by the customer: {website}
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}  
                Client's selected goal: {client_choice}"""),
            expected_output=dedent("""\
                A comprehensive analysis report detailing the technical feasibility, impact, cost-benefit, and integration challenges 
                of AI adoption for {company} in the {industry} sector and {niche} niche, aligned with the goal of {selected_goal}. 
                This report will provide {company} with clear insights into the practicalities and expectations of implementing AI solutions."""),
            async_execution=False,
            agent=agent
        )

    def Ethical_and_Technical_Analysis_Report(self, agent, callback_function):
        return Task(
            description=dedent("""\
                Synthesize the results of the ethic_analysis_task guidelines formulation and ai_technical_analysis_task and impact analysis into a comprehensive report. This report should thoroughly address:

                1. Ethical Considerations: Detail the ethical guidelines and considerations that have been established to ensure the responsible use of AI within the organization. This includes privacy concerns, bias mitigation, and ensuring fairness in AI applications.
                2. Technical Challenges: Analyze the technical hurdles related to AI implementation, including data requirements, algorithmic complexity, and integration with existing infrastructure.
                3. Potential Solutions: Propose solutions and strategies for overcoming identified technical challenges, ensuring successful AI deployment.
                4. Recommendations: Offer recommendations for aligning AI implementation with ethical standards, while also addressing technical feasibility and maximizing organizational benefits.

                The aim is to provide a holistic view of the ethical and technical landscape of AI implementation, facilitating informed decision-making and strategic planning."""),
            expected_output=dedent("""\
                An integrated report that combines ethical considerations and technical analysis related to AI implementation,
                in markdown format, with a consistent style and layout,Key components of the report should include:

                - A detailed examination of the ethical guidelines established for AI use, highlighting how these address key concerns such as privacy, bias, and fairness.
                - An analysis of technical challenges encountered in the deployment of AI solutions, with an emphasis on data, algorithms, and system integration issues.
                - Proposed solutions for overcoming technical obstacles, ensuring the robust and effective implementation of AI technologies.
                - Recommendations for ensuring AI initiatives are ethically responsible and technically feasible, aimed at mitigating risks and leveraging AI for maximum benefit.

                This report should serve as a foundational document for guiding the ethical and technical approach to AI implementation within the organization."""),
            async_execution=False,
            agent=agent,
            callback = callback_function
        )

# IV - infrastructure and solution design

    def Infrastructure_Design_Optimization_Plan_Task(self, agent, industry, niche, client_choice, website):
        return Task(
            description=dedent(f"""\
                Develop an infrastructure design and optimization plan to support the deployment and operation of AI within the {industry} industry, focusing on the {niche} niche. Include:

                1. Hardware and Software Requirements: Specify the necessary hardware and software infrastructure to support AI operations.
                2. Data Storage and Processing: Plan for scalable data storage and processing capabilities to handle AI workloads.
                3. Security Measures: Outline security measures to protect data and AI systems from unauthorized access and cyber threats.
                4. Scalability and Flexibility: Ensure the infrastructure is scalable and flexible to accommodate future AI expansions.

                This plan will serve as a guide for building or upgrading the infrastructure required to effectively support AI applications aligned with the goal of {client_choice}.
                use the website {website} to gather more information.
                
                Selected website by the customer: {website}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}
                Client's selected goal: {client_choice}"""),
            expected_output=dedent("""\
                A detailed infrastructure design and optimization plan, including hardware and software requirements, data storage 
                and processing strategies, security measures, and scalability considerations. This plan will ensure {industry} entities 
                in the {niche} niche are well-prepared for AI deployment and operation aligned with the goal of {selected_goal}."""),
            async_execution=False,
            agent=agent
        )
        
    def AI_Solution_Design_Development_Plan_Task(self, agent, company, industry, niche, client_choice, website):
        return Task(
            description=dedent(f"""\
                Create a detailed AI solution design and development plan for {company} in the {industry} industry, focusing on the {niche} niche. The plan should cover:

                1. Solution Architecture: Designing the architecture of the AI solution, including data flow, model selection, and integration points.
                2. Development Roadmap: Outlining a step-by-step development roadmap, including milestones, deliverables, and timelines.
                3. Resource Allocation: Specifying the resource requirements, including team composition, tools, and technologies needed.
                4. Testing and Validation: Planning for rigorous testing and validation of the AI models to ensure accuracy and reliability.

                This comprehensive plan will guide the development and implementation of the AI solution, ensuring it meets the specified requirements and business objectives aligned with the goal of {client_choice}.
                use the website {website} to gather more information.
                
                Selected website by the customer: {website}
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}
                Client's selected goal: {client_choice}"""),
            expected_output=dedent("""\
                A complete AI solution design and development plan, encompassing solution architecture, a development roadmap, 
                resource allocation, and testing strategies. This plan will facilitate the structured and efficient creation of 
                AI capabilities for {company} aligned with the goal of {selected_goal}."""),
            async_execution=False,
            agent=agent
        )
          
    def Infrastructure_and_Solution_Design_Report(self, agent, callback_function):
        return Task(
            description=dedent("""\
                Create a comprehensive report that details the infrastructure design and optimization plan of infrastructure_design_task report , alongside the AI solution design and development plan devloped in solution_design_task. These plans, developed by the AI infrastructure specialist and solutions architect, should cover:

                1. Infrastructure Specifications: Provide detailed specifications and configurations for the AI infrastructure required to support the AI solutions effectively.
                2. Optimization Plan: Outline strategies for optimizing the existing infrastructure to meet the demands of AI applications, ensuring efficiency and scalability.
                3. AI Solution Design: Detail the design and development plan for the AI solutions, including the choice of algorithms, data processing workflows, and integration with the infrastructure.
                4. Architectural Diagrams: Include architectural diagrams that visualize the infrastructure setup and how the AI solutions fit within it.
                5. Implementation Strategies: Offer recommendations for the implementation of the infrastructure and AI solutions, focusing on best practices, potential challenges, and mitigation strategies.

                The goal is to provide a clear and actionable guide for building and deploying the necessary infrastructure and AI solutions within the organization."""),
            expected_output=dedent("""\
                A detailed report presenting the infrastructure and solution design plans,
                in markdown format, with a consistent style and layout,Key components of the report should include:


                - Technical specifications and configurations for the required AI infrastructure, ensuring it is tailored to support the AI solutions.
                - An optimization plan for enhancing the existing infrastructure to accommodate AI applications, emphasizing efficiency and scalability.
                - A comprehensive AI solution design and development plan, detailing algorithms, data workflows, and system integration.
                - Architectural diagrams illustrating the infrastructure layout and the integration of AI solutions.
                - Implementation strategies that outline best practices, address potential challenges, and suggest solutions for effective deployment.

                This report should serve as a foundational resource for the technical team, guiding the development and implementation of AI infrastructure and solutions."""),
            async_execution=False,
            agent=agent,
            callback = callback_function
        )
       
 # V - Performance Metrics and ROI Analysis
    def Define_Performance_Metrics_Task(self, agent,company):
        return Task(
            description=dedent("""\
                Work with stakeholders to establish clear, measurable performance metrics for each proposed AI solution in the infrastructure_and_solution_design_report. 
                Collaborate closely to ensure these metrics align with the {company}'s strategic goals and are capable of effectively measuring the success and impact of AI implementation. 
                Focus areas should include:

                1. Process Efficiency: Define metrics to quantify improvements in operational processes and workflows as a result of AI integration.
                2. Customer Satisfaction: Establish metrics to measure changes in customer satisfaction levels, utilizing feedback and engagement data.
                3. Sales and Revenue: Identify KPIs related to sales increases or revenue growth attributable to AI-driven enhancements or capabilities.
                4. Cost Reduction: Determine metrics to track cost savings and efficiency gains in various operations, directly linked to AI solutions.
                5. Other Relevant KPIs: Consider additional key performance indicators specific to the organization's sector or operational focus, ensuring a comprehensive evaluation of AI's impact.

                These metrics should serve as a foundational component of the AI strategy, enabling ongoing assessment and fine-tuning of AI initiatives.
                Selected company by the customer: {company}"""),
            expected_output=dedent("""\
                A detailed document outlining the performance metrics for measuring the effectiveness of each AI solution. This document should include:

                - Defined metrics for process efficiency, highlighting specific areas expected to benefit from AI integration.
                - Customer satisfaction measurement approaches, detailing the data sources and feedback mechanisms to be utilized.
                - Sales and revenue growth metrics, explaining the methodology for attributing increases to AI solutions.
                - Cost reduction KPIs, with a clear link between AI applications and operational savings.
                - Any other relevant KPIs tailored to the unique needs and strategic goals of the company.

                This comprehensive set of performance metrics will guide the evaluation of AI implementations, ensuring alignment with the company's strategic objectives and providing a basis for continuous improvement."""),
            async_execution=False,
            agent=agent
        )
        
    def Conduct_ROI_Analysis_Task(self, agent):
        return Task(
            description=dedent("""\
                For each AI solution proposed during the infrastructure_and_solution_design_report, conduct a comprehensive ROI (Return on Investment) analysis. This analysis aims to estimate the financial benefits in comparison to the costs associated with the implementation of each solution. Key aspects to consider include:

                1. Initial Investment: Calculate the upfront costs required to develop, deploy, and integrate the AI solutions into the existing systems and processes.
                2. Operational Costs: Estimate ongoing operational expenses, including maintenance, updates, and any necessary training or support.
                3. Revenue Increases: Project potential revenue growth resulting from the AI solutions, considering factors such as improved sales efficiency, market expansion, and enhanced product or service offerings.
                4. Cost Savings: Assess cost reduction opportunities afforded by the AI solutions, including process optimization, reduced error rates, and operational efficiencies.
                5. Timeframe: Define the timeframe over which the ROI should be calculated, ensuring it aligns with strategic planning cycles and the expected lifespan of the AI solutions.

                The ROI analysis should provide a clear financial framework to evaluate the viability and impact of each AI initiative, facilitating informed decision-making and strategic investment."""),
            expected_output=dedent("""\
                A detailed ROI analysis report for each proposed AI solution, including:

                - Calculations of initial investment and ongoing operational costs.
                - Projections of potential revenue increases and cost savings.
                - A comprehensive assessment of the net financial benefit of implementing the AI solutions.
                - Recommendations on prioritizing AI investments based on their projected ROI.

                This report should serve as a critical tool for stakeholders to assess the financial implications of AI initiatives, guiding resource allocation and strategic planning to maximize return on investment."""),
            async_execution=False,
            agent=agent
        )

    def Prioritize_AI_Initiatives_Task(self, agent):
        return Task(
            description=dedent("""\
                Utilize the insights gathered from define_performance_metrics_task and conduct_roi_analysis_task tasks to prioritize AI initiatives. This task involves:

                1. Impact Analysis: Evaluate the potential impact of each AI initiative on the company's strategic goals, focusing on areas such as efficiency gains, customer satisfaction, and market competitiveness.
                2. ROI Consideration: Assess the estimated Return on Investment for each AI project, prioritizing those with the highest financial benefits relative to costs.
                3. Resource Allocation: Determine the optimal allocation of resources, including budget, personnel, and technology, to ensure successful implementation of prioritized AI initiatives.
                4. Value Maximization: Aim to maximize value for the company by selecting AI projects that offer significant improvements in operations, customer experience, or revenue generation.

                The goal is to establish a clear priority order for AI initiatives, based on their alignment with business objectives, potential impact, and financial viability."""),
            expected_output=dedent("""\
                A prioritized list of AI initiatives, including:

                - A rationale for the priority ranking, based on performance metrics, potential impact, and ROI analysis.
                - A resource allocation plan that outlines how the company's assets will be distributed among the prioritized projects.
                - Strategic recommendations for implementing the high-priority AI initiatives, with an emphasis on achieving quick wins and long-term value.

                This prioritization report will guide the company in focusing its efforts on AI projects that are most likely to drive significant benefits and contribute to the achievement of strategic goals."""),
            async_execution=False,
            agent=agent
        )

    def performance_metrics_and_ROI_analysis_report_task(self, agent, company,callback_function):
        return Task(
            description=f"""\
                Generate a detailed performance metrics and Return on Investment (ROI) analysis report for {company}. 
                This report should synthesize the findings from Conduct_ROI_Analysis_Task,Conduct_ROI_Analysis_Task, Prioritize_AI_Initiatives_Task. It should include:
                - Analysis of existing KPIs and potential metrics for AI implementation.
                - Financial implications of AI adoption, including initial investment, expected returns, and payback period.
                - Insights into the impact of AI initiatives on revenue, cost savings, customer satisfaction, and productivity.
                """,
            expected_output="""\
                A comprehensive performance metrics and ROI analysis report for {company}, presenting the findings,
                in markdown format, with a consistent style and layout,Key components of the report should include:

                from the data researcher's analysis in a clear and professional manner. The report should provide actionable 
                insights into the financial implications of AI adoption and the potential impact on business operations. 
                This report will serve as a crucial resource for decision-making and strategic planning for AI initiatives.
                """,
            async_execution=False,
            agent=agent,
            callback = callback_function
        )

# VI - Project framework 
          
    def AI_Project_Management_Coordination_Framework_Task(self, agent, company, industry, niche, client_choice, website):
        return Task(
            description=dedent(f"""\
                based on initial_research_and_analysis_report, strategy_planning_report_task, ethical_and_technical_analysis_report, infrastructure_and_solution_design_report, 
                performance_metrics_and_roi_analysis_report, Develop an AI project management and coordination framework for {company} in the {industry} industry, focusing on the {niche} niche. This framework will include:

                1. Project Planning: Defining project objectives, scope, deliverables, and timelines.
                2. Team Coordination: Establishing roles, responsibilities, and communication channels for effective team collaboration.
                3. Risk Management: Identifying potential risks and developing mitigation strategies to ensure project success.
                4. Monitoring and Evaluation: Implementing mechanisms for monitoring project progress and evaluating outcomes against predefined metrics.

                The framework will ensure the smooth execution of AI projects aligned with the goal of {client_choice}.
                use the website {website} to gather more information.
                
                Selected website by the customer: {website}
                Selected company by the customer: {company}
                Selected industry by the customer: {industry}
                Selected niche by the customer: {niche}
                Client's selected goal: {client_choice}"""),
            expected_output=dedent("""\
                A comprehensive AI project management and coordination framework, including project planning, team coordination, risk management, 
                and monitoring mechanisms. This framework will facilitate the successful execution of AI initiatives aligned with the goal of {selected_goal}."""),
            async_execution=False,
            agent=agent
        )

# VII - Final report

    def Final_Presentation_Report(self, agent, callback_function):
        return Task(
            description=dedent("""\

                Compile all previous reports : initial_research_and_analysis_report, strategy_planning_report_task, ethical_and_technical_analysis_report, infrastructure_and_solution_design_report, 
                performance_metrics_and_roi_analysis_reportinto and the framework generated in the project_management_framework_task task, in a final presentation report. This document is designed to provide a comprehensive overview of the entire AI consultation process, encompassing:

                1. Process Overview: Summarize the AI consultation process, outlining the steps taken, methodologies applied, and key areas of focus.
                2. Key Findings: Highlight the critical insights and findings from each phase of the consultation, including industry analysis, competitive landscape, ethical and technical assessments, and infrastructure and solution design.
                3. Recommendations: Consolidate the recommendations provided throughout the consultation, emphasizing strategic initiatives, ethical considerations, technical solutions, and infrastructure optimization.
                4. Proposed Solutions: Detail the proposed AI solutions, including their design, intended benefits, and impact on the organization.
                5. Next Steps: Outline actionable next steps for implementing the AI strategies and solutions recommended by the consultation team.

                The report should be polished and professional, suitable for presentation to clients, company executives, or consumers, effectively communicating the value and potential impact of the proposed AI initiatives."""),
            expected_output=dedent("""\
                A polished and professional presentation report that summarizes the entire AI consultation project,
                 in markdown format, with a consistent style and layout,Key components of the report should include:

                - A clear overview of the AI consultation process and methodologies used.
                - Summarized key findings from each report, highlighting essential insights and implications for the organization.
                - Consolidated recommendations for AI adoption, ethical considerations, and technical strategies.
                - Detailed proposed solutions, including AI infrastructure and applications, designed to meet organizational goals.
                - A roadmap of next steps for implementing the AI initiatives, ensuring readiness for future challenges and opportunities.

                This comprehensive report serves as the culmination of the AI consultation effort, showcasing the insights, strategies, and deliverables generated by the team, and providing a clear path forward for the organization's AI journey."""),
            async_execution=False,
            agent=agent,
            callback=callback_function
        )

