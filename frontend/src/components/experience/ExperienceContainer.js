import React, { Component } from 'react';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Collapse from 'react-bootstrap/Collapse';

import "../../styles/experience.css"


class ExperienceContainer extends Component {
	constructor(props) {
		super(props);

		this.state = {
			pyOpen: false,
			cOpen: false,
			cppOpen: false,
			csOpen: false,
			jsOpen: false,
			swiftOpen: false,
			reactOpen: false,
			taOpen: false,
			blogOpen: false,
			gwOpen: false,
			sotlOpen: false,
			gameOpen: false
		}
	}
	render() {
		return (
			<Container>
				<Row className="justify-content-md-center">
					<Col>
						<h1 style={{textAlign:"center"}}><b>Technical Experience</b></h1>
					</Col>
				</Row>
				<hr />
				<Row>
					<Col style={{textAlign:"center"}}>
						<p>This page will outline and display various techical projects and experiences I have taken part in. You can also download my <a target="_blank" rel="noopener noreferrer" href="https://nigelhaney.me/imgs/resume.pdf">resume here.</a><br />Click on the various sections below to learn more about my various skills.</p>
					</Col>
				</Row>
				<hr />
				<Row>
					<Col sm={6}>
						<h2><b><u>Programming Languages</u></b></h2>

						<span onClick={() => this.setState({pyOpen: !this.state.pyOpen})} 
										aria-controls="py-collapse-text"
										aria-expanded={this.state.pyOpen}
										className="dropdown-button"><h3>Python<i style={{color:"grey"}} className={this.state.pyOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.pyOpen}>
							<div id="py-collapse-text">
								I have taught this language and used it extensively with many different frameworks for both projects and competitive programming. My primary and most comfortable language.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({cOpen: !this.state.cOpen})} 
										aria-controls="c-collapse-text"
										aria-expanded={this.state.cOpen}
										><h3 className="dropdown-button">C<i style={{color:"grey"}} className={this.state.cOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.cOpen}>
							<div id="c-collapse-text">
								Not my favorite language, but I have used it extensively as it was the main language used in curriculum during my education. I have used this language in a wide variety of contexts, such as embedded systems, networking, security, and many more.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({cppOpen: !this.state.cppOpen})} 
										aria-controls="cpp-collapse-text"
										aria-expanded={this.state.cppOpen}
										className="dropdown-button"><h3>C++<i style={{color:"grey"}} className={this.state.cppOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.cppOpen}>
							<div id="cpp-collapse-text">
								Another language I used extensively in school, as it was the second most common language in my coursework (used to teach OOP concepts). I have done many projects in this language from computational biology to distributed systems. One of my future goals is to learn modern C++, as this was never covered during my education.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({csOpen: !this.state.csOpen})} 
										aria-controls="cs-collapse-text"
										aria-expanded={this.state.csOpen}
										className="dropdown-button"><h3>C#<i style={{color:"grey"}} className={this.state.csOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.csOpen}>
							<div id="cs-collapse-text">
								I have used C# quite a bit, but not in a lot of contexts. I primarily used it for game programming with Unity. I enjoy using it, and I feel that it would be easy for me to transfer knowledge of the language to different types of work besides game programming in the future.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({jsOpen: !this.state.jsOpen})} 
										aria-controls="js-collapse-text"
										aria-expanded={this.state.jsOpen}
										className="dropdown-button"><h3>JavaScript (Vanilla)<i style={{color:"grey"}} className={this.state.jsOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.jsOpen}>
							<div id="js-collapse-text">
								I have used vanilla JS quite a lot this past year to make quick web pages and games. Although I have used it a lot, I feel that my knowledge is lacking in front-end development and all of the code I have wrote was not the highest quality. I most likely will only use vanilla JS in the future for fun in quick projects.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({swiftOpen: !this.state.swiftOpen})} 
										aria-controls="swift-collapse-text"
										aria-expanded={this.state.swiftOpen}
										className="dropdown-button"><h3>Swift 4<i style={{color:"grey"}} className={this.state.swiftOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.swiftOpen}>
							<div id="swift-collapse-text">
								Similar to vanilla JS, I have used it quite a lot in the past year for making quick mobile apps. I find it quite fun working in the Swift ecosystem, but I do not know exactly what it takes to write high quality Swift code. I hope to improve my Swift skills in the future if I find myself working on an iOS focused project, as mobile app development interests me quite a bit.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({reactOpen: !this.state.reactOpen})} 
										aria-controls="react-collapse-text"
										aria-expanded={this.state.reactOpen}
										className="dropdown-button"><h3>JavaScript (React)<i style={{color:"grey"}} className={this.state.reactOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.reactOpen}>
							<div id="react-collapse-text">
								I have only just started working with React JS but I enjoy it quite a bit. The front-end of this website is developed fully using React. I look forward to learning more about it as this site grows and hopefully branch out into using React Native for my next mobile app endeavor.
							</div>
						</Collapse>
					</Col>
					
					

					<Col sm={6}>
						<h2><b><u>Experiences / Projects</u></b></h2>
						<span onClick={() => this.setState({taOpen: !this.state.taOpen})} 
										aria-controls="ta-collapse-text"
										aria-expanded={this.state.taOpen}
										className="dropdown-button"><h3>Introduction to Computer Programming Teaching Assistant<i style={{color:"grey"}} className={this.state.taOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.taOpen}>
							<div id="ta-collapse-text">
								In my last semester of school I was a TA for an introductory computer science class. I conducted one three hour lab session per week and held an office hour once a week for students to come in if they needed help. The most important thing that this experience taught me was how to become a good leader and how to concisely explain programming concepts to those that don't understand them right away. I also learned that teaching content strengthened my own knowledge, which is one of the primary reasons I made a blog on this website. In the future I will make a blog post about the tactics that I used to teach programming to complete beginners.
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({blogOpen: !this.state.blogOpen})} 
										aria-controls="blog-collapse-text"
										aria-expanded={this.state.blogOpen}
										className="dropdown-button"><h3>This website<i style={{color:"grey"}} className={this.state.blogOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.blogOpen}>
							<div id="blog-collapse-text">
								This website that you are currently on is one of the biggest projects I have taken part in. The reason I made this site is to further my knowledge after I graduated by taking on a project that will teach me relevant skills to working in the industry. This website features both a responsive frontend and a RESTful API backend that can dynamically serve the content. More information about the technical details of the site can be found in my blog post <a target="_blank" rel="noopener noreferrer" href="/blog/Blog Engine Intro">here.</a> If you are interested in viewing some of the source code of this site, you may view it <a target="_blank" rel="noopener noreferrer" href="https://github.com/nhaney/portfoliosite">here.</a>
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({gwOpen: !this.state.gwOpen})} 
										aria-controls="gw-collapse-text"
										aria-expanded={this.state.gwOpen}
										className="dropdown-button"><h3>GroundworksWSU<i style={{color:"grey"}} className={this.state.gwOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.gwOpen}>
							<div id="gw-collapse-text">
								GroundworksWSU is a mobile app designed to make walking on campus safer for students during the winter time. The goal of this app is to allow students and faculty to notify the Facility Services of icy sidewalks so they can target problem areas quicker. Users can use geolocation or search for a location to report, rate the condition, and take an optional photo of the condition. After a user has reported the condition, the report is logged in a database and then a operator can see all of the reports from a web view. A technical blog post write up of this project can be found <a target="_blank" rel="noopener noreferrer" href="/blog/GroundworksApp">here.</a> You may also find some of the source code of the project <a target="_blank" rel="noopener noreferrer" href="https://github.com/nhaney/GroundworksWSU">here.</a>
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({sotlOpen: !this.state.sotlOpen})} 
										aria-controls="sotl-collapse-text"
										aria-expanded={this.state.sotlOpen}
										className="dropdown-button"><h3>Stay Off the Line!<i style={{color:"grey"}} className={this.state.sotlOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.sotlOpen}>
							<div id="sotl-collapse-text">
								"Stay Off the Line!" is an HTML5 web game made during the js13k game competition of 2018. I entered the competition because I was interested in learning more JavaScript fundamentals and I thought it would be a good way to inspire me to finish a project. The time limit was one month, and the size limit of the game was 13kb. I learned many things about making a game engine from scratch as well as working with the HTML5 canvas. Overall I finished 121st out of 274 entries. Not good enough to get the free t-shirt, but good enough to make me feel happy with the work I put in. I go into more detail on the game in a blog post <a target="_blank" rel="noopener noreferrer" href="/blog/js13k2018">here.</a> If you would like to play the game, you can do so <a target="_blank" href="/games/fish">here,</a> and if you would like to view the source code for this project, it is on Github <a target="_blank" rel="noopener noreferrer" href="https://github.com/nhaney/stayOffTheLine"> here.</a>
							</div>
						</Collapse>
						<hr />

						<span onClick={() => this.setState({gameOpen: !this.state.gameOpen})} 
										aria-controls="game-collapse-text"
										aria-expanded={this.state.gameOpen}
										className="dropdown-button"><h3>Classroom Gamification<i style={{color:"grey"}} className={this.state.gameOpen ? 'fa fa-caret-up' : 'fa fa-caret-down'}></i></h3>
						</span>
						<Collapse in={this.state.gameOpen}>
							<div id="game-collapse-text">
								At my school, every student who graduated with a B.S. in Computer Science had to participate in a Senior Design project. My project was with a group of four other students and we set out to create a classroom-independent game that can encourage educational growth without featuring any educational material. This project is ongoing, but in my time with it I learned what it takes to take on a very large pre-existing codebase, work in a team (software engineering practices, source control, etc.), and what it takes to step up in a leadership role and organize people to work towards an end goal. A general write-up on the ideas of this project can be found in my blog post <a target="_blank" rel="noopener noreferrer" href="/blog/gamification">here.</a>
							</div>
						</Collapse>
					</Col>
				</Row>
			</Container>
		);
	}
}


export default ExperienceContainer;
