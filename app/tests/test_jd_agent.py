from app.agents.jd_agent import extract_jd

if __name__ == "__main__":
    job_source = {
        "type": "text",
        "value": """
About the job

Job Profile: - Software Development Engineer I

Years of Experience: 1 - 3

Location: Bangalore

Position Overview:

SDE I in Swiggy plays a key role in owning end to end design/architecture of a complex system/team they are assigned to. They co-own the technology vision of the respective team and significantly contribute to the overall success of the team. They partner with the product & business teams to understand the product features and specifications, translate them into high level and low-level design thereby facilitating the team in design and development of mission critical applications.

What qualities are we looking for?

    B Tech/M Tech in Computer Science or equivalent from a reputed college with minimum 1 – 3 years of experience in product development company.
    Strong technical aptitude and good knowledge of CS fundamentals.
    Sound knowledge and application of algorithms and data structures with space and me complexities
    Strong design skills involving data modeling and low level class design
    Good knowledge of object oriented programming and design pa erns
    Proficiency in programming language - Java or Golang
    Follow industry coding standards and responsible for writing maintainable, scalable & eﬃcient code to solve business problems
    Hands-on experience of working with databases and Linux/Unix platform
    Follow SDLC in agile environment and collaborate with multiple cross functional teams to drive on- me deliveries

What will you get to do here?

    Coming up with best practices to help the team achieve their technical tasks and continually thrive in improving the technology of the product/team.
    Driving the adoption of best practices & regular participation in code reviews, design reviews, architecture discussions.
    Experiment with new & relevant technologies and tools, and drive adoption while measuring yourself on the impact you can create.
    Implementation of long term technology vision for your team.
    Creating architectures & designs for new solutions around existing/new areas
    Decide technology & tool choices for your team & be responsible for them.

We are an equal opportunity employer and all qualified applicants will receive consideration for employment without regard to race, colour, religion, sex, disability status, or any other characteristic protected by the law.
"""
    }

    result = extract_jd(job_source)

    print("\n=== Extracted Job Description ===")
    print(result)